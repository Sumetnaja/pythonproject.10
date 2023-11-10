# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/extend (x)/read (r)

try :
    f_iot = open('iot4.txt' , 'w' , encoding='utf-8')

    f_iot.write('wow...')
    f_iot.write('Hi...\n')
    f_iot.write('สวัสดี...\n')

    f_iot.close()
except FileExistsError :
    print('กรุณาเปลี่ยนชื่อไฟล์ใหม่เพราะซ้ำ...')


