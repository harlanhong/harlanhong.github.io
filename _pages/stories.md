--- 
layout: archive 
title: "Stories" 
permalink: /stories/ 
author_profile: true 
--- 
{% include base_path %} 
{% for post in site.stories %} 
    {% include archive-single.html %} 
{% endfor %}
