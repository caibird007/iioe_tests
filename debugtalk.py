#coding: utf-8
import time
import langid                             #引入langid模块

def sleep(n_secs):
    time.sleep(n_secs)

def get_category_list():
    return ['学科课程','职业教育课程','职业教育课程']


def is_courses_open(course_list):
    for course in course_list:
        if course['status'] != "OPEN":
            return False
    return True


def is_lang_fr(str):
    lang = langid.classify(str)
    return True if lang == 'fr' else False

def is_lang_en(str):
    lang = langid.classify(str)
    return True if lang == 'en' else False

def is_lang_ch(str):
    lang = langid.classify(str)
    return True if lang == 'zh' else False

def get_list_len(_list):
    return len(_list)

def is_courses_fr(course_list):
    for course in course_list:
        rootCategoryName = course['rootCategoryName'] if 'rootCategoryName' in course else ''
        lang_code = course['languageCode']
        if  lang_code != 'fr':
            return False
    return True

def is_courses_en(course_list):
    for course in course_list:
        rootCategoryName = course['rootCategoryName'] if 'rootCategoryName' in course else ''
        lang_code = course['languageCode']
        if lang_code != 'en':
            return False
    return True

def is_courses_cn(course_list):
    for course in course_list:
        rootCategoryName = course['rootCategoryName'] if 'rootCategoryName' in course else ''
        lang_code = course['languageCode']
        if lang_code != 'cn':
            return lang_code
    return True



def date2timestamp(date):
    print(date)
    timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

#if __name__ == '__main__':
#    print date2timestamp("2020-03-29 13:48:52")

