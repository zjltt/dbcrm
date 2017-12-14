#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
使用方式：
    all_count = models.UserInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('p'),10,all_count,request.path_info)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request,'users2.html',{'user_list':user_list,'page_info':page_info})
"""
class PageInfo(object):
    # 当前页以及每一页相应显示多少条目
    def __init__(self,current_page,per_page_num,all_count,base_url,page_range=7):
        """
        :param current_page: 当前页
        :param per_page_num: 每页显示的数据的条数
        :all_count: 数据库中样本的总个数
        :base_url为生成的页码标签的前缀
        :page_range:页面最多显示的页码个数
        :我们可以根据自己的情况进行定制相应的信息,存到page_list = []里面
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = int(1)
        # 定义两个属性
        self.current_page = current_page
        self.per_page_num = per_page_num
        self.all_count = all_count
        a,b = divmod(all_count,per_page_num)
        # 根据余数情况进行分析:all_page为总页数
        if b != 0:
            self.all_page = a + 1
        else:
            self.all_page = a
        self.base_url = base_url
        self.page_range = page_range

    # 获取起始页
    def start(self):
        return (self.current_page -1)* self.per_page_num

    #获取结尾页
    def end(self):
        return self.current_page*self.per_page_num

    def page_str(self):
        """
        在html页面中帮我们显示相应的页码信息
        :return:
        """
        page_list = []
        if self.current_page <= 1:
            prev = '<li><a href="#">上一页</a></li>'
        else:
            prev = '<li><a href="%s?p=%s">上一页</a></li>'%(self.base_url,self.current_page-1)
        page_list.append(prev)
        """
        在中间的这个位置写页码:遍历页数,存到集合集合中
        """
        #假设我的总页数小于规定的的页数范围,else...
        if self.all_page <= self.page_range:
            start = 1
            end = self.all_page + 1
        else:
            # 随后在根据当前页进行判断
            if self.current_page > int(self.page_range/2):
                if (self.current_page + int(self.page_range/2)) > self.all_page:
                    start = self.all_page - self.page_range + 1
                    end = self.all_page + 1
                else:
                    start = self.current_page - int(self.page_range / 2)
                    end = self.current_page + int(self.page_range / 2) + 1
            else:
                start = 1
                end = self.page_range + 1

        for i in range(start,end):
            if self.current_page == i:
                temp = '<li class="active"><a href="%s?p=%s">%s</a></li>'%(self.base_url,i,i)
            else:
                temp = '<li><a href="%s?p=%s">%s</a></li>'%(self.base_url,i,i)
            page_list.append(temp)

        if self.current_page >= self.all_page:
            nex = '<li><a href="#">下一页</a><span><a href="/hosts/">返回首页</a></span></li>'
        else:
            nex = '<li><a href="%s?p=%s">下一页</a><span><a href="/hosts/">返回首页</a></span></li>' % (
                self.base_url, self.current_page + 1)
        page_list.append(nex)

        #将当前页和后一页进行拼接操作
        return "".join(page_list)