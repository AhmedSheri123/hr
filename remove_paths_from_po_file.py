import polib
import re

def clean_po_file(file_path):
    # فتح ملف .po باستخدام polib
    po_file = polib.pofile(file_path)
    
    # المرور على كل مدخل في ملف po
    for entry in po_file:
        # print(entry.occurrences)
        # إزالة المسارات من التعليقات التي تبدأ بـ '#:' 
        entry.occurrences = tuple(line for line in entry.occurrences if isinstance(line, str) and not line.startswith('#:'))
        entry.msgstr = ''

    
    # حفظ التغييرات في ملف po
    po_file.save(file_path)

# تحديد مسار ملف .po
locale_path = 'F:/mostql/rady-made-projects/HR/horilla-master2/horilla-master/locale/ar/LC_MESSAGES/django.po'

# تنظيف الملف
clean_po_file(locale_path)
