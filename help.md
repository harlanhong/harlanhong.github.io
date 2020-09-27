### 添加导航栏
-	在_config.yml中line178添加collections
-	在_config.yml中line196添加default
-	在_data/navigation.yml中添加相应的栏目
-	到_pages中添加相应名称的md或html文件，写入如下文档：
``` python
	--- 
	layout: archive 
	title: "XXX" 
	permalink: /XXX/ 
	author_profile: true 
	--- 
	{% include base_path %} 
	{% for post in site.XXX %} 
	    {% include archive-single.html %} 
	{% endfor %}

```
-	在根目录下创建_xxx文件夹
	-在_xxx文件下添加文件_doc1，开头写入如下代码引用
``` python
---
title: "白鹿原"
collection: reading
type: "Reading"
permalink: /reading/bai_lu_yuan
date: 2017-6-1
---
```