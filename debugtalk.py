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

def is_resources_pdf(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['formatCode'] != 'PDF':
            return False
    return True

def is_resources_video(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['formatCode'] != 'VIDEO':
            return False
    return True

def is_resources_word(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['formatCode'] != 'WORD':
            return False
    return True

def is_resources_other(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['formatCode'] != 'OTHER':
            return False
    return True

def is_resources_IIOE_DOCUMENTS(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['categoryCode'] != 'IIOE_DOCUMENTS':
            return False
    return True

def is_resources_IIOE_TRAINING_MATERIALS(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['categoryCode'] != 'IIOE_TRAINING_MATERIALS':
            return False
    return True

def is_resources_ICT_ED_PUBLICATIONS(resource_list):
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['categoryCode'] != 'ICT_ED_PUBLICATIONS':
            return False
    return True

def is_in_cn_library_categrois(resource_list):
    category_list = ["IIOE文档", "IIOE培训材料", "ICT/教育出版物"]
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['categoryName'] not in category_list:
            return False
    return True

def is_in_fr_library_categrois(resource_list):
    category_list = ["Documents de l'IIOE", "Ressouces de formation de l'IIOE", "Publications sur les TIC"]
    for resource in resource_list:
        if resource['categoryName'] not in category_list:
            return False
    return True

def is_in_en_library_categrois(resource_list):
    category_list = ['IIOE Documents','IIOE Training Materials', 'ICT-ED Publications']
    if not resource_list:
        return True
    for resource in resource_list:
        if resource['categoryName'] not in category_list:
            return False
    return True

def is_networks_college(network_list):
    if not network_list:
        return True
    for network in network_list:
        if network['type'] != 'COLLEGE':
            return False
    return True

def search_Shenzhen_Polytechnic_from_college(network_list, lang='zh-CN'):
    if not network_list:
        return True
    for network in network_list:
        if network['name'] in ['Shenzhen Polytechnic','深圳职业技术学院','Institut Polytechnique de Shenzhen']:
            if lang == 'zh-CN':
                if network['country'] == '中国':
                    return True
                else:
                    return False
            elif lang == 'en-US':
                if network['country'] == 'China':
                    return True
                else:
                    return False
            elif lang == 'fr-FR':
                if network['country'] == 'Chine':
                    return True
                else:
                    return False
            else:
                return False
 
    return False


def search_cio_times_from_enterprise(network_list, lang='zh-CN'):
    if not network_list:
        return True
    for network in network_list:
        if network['name'] in ['CIO Times','CIO时代学院'] :
            if lang == 'zh-CN':
                if network['country'] == '奥兰群岛':
                    return True
                else:
                    return False
            elif lang == 'en-US':
                if network['country'] == 'Aland Islands':
                    return True
                else:
                    return False
            elif lang == 'fr-FR':
                if network['country'] == 'Îles Aland':
                    return True
                else:
                    return False
            else:
                return False
 
    return False

def is_networks_normal(network_list):
    if not network_list:
        return True
    for network in network_list:
        if network['status'] != 'NORMAL':
            return False
    return True


def is_networks_enterprise(network_list):
    if not network_list:
        return True
    for network in network_list:
        if network['type'] != 'ENTERPRISE':
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

