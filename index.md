---
layout: home
title: BC Daily Digest
---

# Přehled novinek ze světa programování v AL

{% for post in site.posts %}
  <article>
    <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
    <p>{{ post.date | date: "%d. %m. %Y" }}</p>
  </article>
{% endfor %}
