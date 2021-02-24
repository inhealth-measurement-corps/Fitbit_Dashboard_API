import os
import pymssql


def get_last_sync_date(patient_population):
    conn = pymssql.connect(server= 'inhealth.wse.jhu.edu', user='WIN\\WSE-MeasurementCorps', password='KwGCyTn97nSkFGaFnwP', database='master')
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT study_id, last_sync_time FROM mmcfitbit.users JOIN mmcfitbit.devices ON mmcfitbit.users.fitbit_uid = mmcfitbit.devices.fitbit_uid WHERE mmcfitbit.users.patient_population = %s", (patient_population))
    arr = cursor.fetchall()
    conn.close()
    return arr
print(get_last_sync_date("PC"))