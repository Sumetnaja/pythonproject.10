# File Handling
# ไฟล์ การจัดการ
# คือ การทำงานกับไฟล์
# การเปิดไฟล์ write (w)/extend (x)/read (r)

f_iot = open('iot1.txt' , 'w' , encoding='utf-8')

f_iot.write('wow...')
f_iot.write('Hello naa jaa\n')
f_iot.write('Hello naa jaaa\n')

f_iot.close()



