import scrapy

class TestZhiPinSpider(scrapy.Spider):

    name = "TestZhiPinSpider"
    start_urls = [
        # "https://www.zhipin.com/c101210100-p100203/"
        # "https://www.zhipin.com/job_detail/1411294670.html"
        "https://www.zhipin.com/job_detail/1411310811.html"
    ]

    def parse(self, response):
        print(" stsParse ")
        selector = scrapy.Selector(response)

        # 列表页解析
        # job_list = selector.xpath("//div[@class='job-list']/ul/li/a")
        # for job_content in job_list :
        #     x = job_content.extract()
        #     print(" x: "+x)
        #     url = job_content.xpath("./@href").extract_first()
        #     print(" url: "+url)
        #
        #     job_city_age_adu \
        #         = job_content.xpath("./div[@class='job-primary']/div[@class='info-primary']/p/text()").extract()
        #
        #     for job_city_age_adu_content in job_city_age_adu:
        #         print("job_city_age_adu_content: "+job_city_age_adu_content)
        #
        #     print("job_city_age_adu_content: " + job_city_age_adu_content[0] )
        #     print(" -------------------------------------------------------------- ")

        # 详情页
        job_primary = selector.xpath("//div[@class='job-primary']")
        info_primary = job_primary.xpath("./div[@class='info-primary']")
        info_company = job_primary.xpath("./div[@class='info-company']")

        job_time = info_primary.xpath("./div[@class='job-author']/span/text()").extract_first()
        job_type = info_primary.xpath("./div[@class='name']/text()").extract_first()
        job_pay = info_primary.xpath("./div[@class='name']/span/text()").extract_first()

        job_city_age_edu = info_primary.xpath("./p/text()").extract()
        job_city_age_edu_str = ""
        for job_city_age_edu_content in job_city_age_edu:
            job_city_age_edu_str = job_city_age_edu_str +" "+ job_city_age_edu_content

        job_city = ""
        job_age = ""
        job_edu = ""
        job_city_age_edu_length = len(job_city_age_edu)
        if job_city_age_edu_length >= 1:
            job_city = job_city_age_edu[0]
        if job_city_age_edu_length >= 2:
            job_age = job_city_age_edu[1]
        if job_city_age_edu_length >= 3:
            job_edu = job_city_age_edu[2]

        job_company_info = info_company.xpath("./p/text()").extract()
        job_company_info_str = ""
        for job_company_info_content in job_company_info:
            job_company_info_str = job_company_info_str +" "+ job_company_info_content

        #公司规模可能为空
        job_company_name = ""
        job_company_type = ""
        job_company_kind = ""
        job_company_pn = ""
        job_company_info_length = len(job_company_info)
        if job_company_info_length >= 1:
            job_company_name = job_company_info[0]
        if job_company_info_length >= 2:
            job_company_type = job_company_info[1]
        if job_company_info_length >= 3:
            job_company_kind = job_company_info[2]
        if job_company_info_length >= 4:
            job_company_kind = job_company_info[2]
            job_company_pn = job_company_info[3]


        job_company_add = selector.xpath("//div[@class='location-address']/text()").extract_first()
        job_company_long_lat = selector.xpath("//div[@id='map-container']").xpath('@data-long-lat').extract_first()
        job_desc_list = selector.xpath("//div[@class='text']/text()").extract()
        job_desc = ""
        for job_desc_content in job_desc_list:
            job_desc = job_desc +  job_desc_content

        print("job_time:  "+job_time)
        print("job_type:  " + job_type)
        print("job_pay:  " + job_pay)
        print("job_city:  " + job_city)
        print("job_age:  " + job_age)
        print("job_edu:  " + job_edu)
        print("job_company_info_str:  " + job_company_info_str)



        print("job_company_name:  " + job_company_name)
        print("job_company_type:  " + job_company_type)
        print("job_company_kind:  " + job_company_kind)
        print("job_company_pn:  " + job_company_pn)
        print("job_company_info_str:  " + job_company_info_str)

        print("job_company_add:  " + job_company_add)
        print("job_company_long_lat:  " + job_company_long_lat)
        print("job_desc:  " + job_desc)
