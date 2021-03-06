# -*- coding:utf-8 -*-
# !/usr/bin/python

from dbutil import DBUtil
from dateutil import DateUtil
import MySQLdb
import datetime
import traceback

"""
用来检查依赖任务运行的时间是否正确
job_name,start_time,dep_job,start_time
"""


def get_dependency(cursor, job_name, dep_jobs):
    dep_sql = "select job_name,dependency_job from t_etl_job_dependency where job_name = %s"
    cursor.execute(dep_sql, (job_name,))
    deps = cursor.fetchall()
    for dep_job in deps:
        dep_jobs.add(dep_job["dependency_job"])
        get_dependency(cursor, dep_job["dependency_job"], dep_jobs)
    return dep_jobs

if __name__ == '__main__':

    dbUtil = DBUtil()
    connection = dbUtil.get_connection()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)

    today = DateUtil.get_now_fmt()
    job_sql = "select job_name,last_start_time,last_end_time from t_etl_job where 1=1 "

    cursor.execute(job_sql + " and last_run_date=%s", (today,))
    jobs = cursor.fetchall()

    count = 0
    failed = 0
    error = 0
    for job in jobs:
        job_name = job["job_name"]
        job_start_time = datetime.datetime.strptime(job["last_start_time"], "%Y-%m-%d %H:%M:%S")
        dep_jobs = set()
        get_dependency(cursor, job_name, dep_jobs)
        for dep_job in dep_jobs:
            cursor.execute(job_sql + " and job_name = %s", (dep_job,))
            dep_job_detail = cursor.fetchone()
            #print dep_job_detail
            try:
                dep_job_end_time = datetime.datetime.strptime(dep_job_detail["last_end_time"], "%Y-%m-%d %H:%M:%S")
                duration = (job_start_time - dep_job_end_time).total_seconds()
                if duration <= 0:
                    failed += 1
                    print job_name, job_start_time, dep_job, dep_job_end_time, str(duration)
            except Exception as e:
                print traceback.format_exc()
                print "job->", job
                print "dep_job->", dep_job_detail
                error += 1
        count += 1
    print "check:" + str(count) + " jobs failed:" + str(failed) + " exception:" + str(error)
