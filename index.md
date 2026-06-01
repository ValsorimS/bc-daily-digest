---
layout: home
title: BC Daily Digest
---

# Přehled novinek ze světa programování v AL

{%- comment -%}
Řadíme podle data PUBLIKACE článku (original_date) sestupně – nejnovější
obsah nahoře. Hranice "nového" článku: původní článek z posledních 30 dní
(30*24*3600 s); starší jdou do sbaleného archivu.
Pozor: HTML níže musí být na sloupci 0 – odsazení o 4+ mezery by kramdown
vykreslil jako blok kódu místo HTML.
{%- endcomment -%}
{% assign now_ts = 'now' | date: '%s' | plus: 0 %}
{% assign cutoff_ts = now_ts | minus: 2592000 %}
{% assign sorted = site.posts | sort: 'original_date' | reverse %}

## Nové články

{% assign found_new = false -%}
{% for post in sorted -%}
{%- assign is_new = false -%}
{%- if post.original_date -%}
{%- assign ots = post.original_date | date: '%s' | plus: 0 -%}
{%- if ots >= cutoff_ts %}{% assign is_new = true %}{% endif -%}
{%- endif -%}
{%- if is_new -%}
{%- assign found_new = true %}
<article class="card post-card">
<h2 class="post-card__title"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
<p class="post-card__meta">Zpracováno {{ post.date | date: "%d. %m. %Y" }}{% if post.original_date %} · původní článek z {{ post.original_date | date: "%d. %m. %Y" }}{% endif %} {% include verdict-badge.html post=post %}</p>
<div class="excerpt">{{ post.excerpt }}</div>
<a class="post-card__more" href="{{ site.baseurl }}{{ post.url }}">Číst dále →</a>
</article>
{% endif -%}
{% endfor -%}
{% unless found_new %}<p><em>Zatím žádné nové články.</em></p>{% endunless %}

<details class="archive">
<summary>Z archivu</summary>
{% for post in sorted -%}
{%- assign is_new = false -%}
{%- if post.original_date -%}
{%- assign ots = post.original_date | date: '%s' | plus: 0 -%}
{%- if ots >= cutoff_ts %}{% assign is_new = true %}{% endif -%}
{%- endif -%}
{%- unless is_new %}
<article class="card post-card">
<h2 class="post-card__title"><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
<p class="post-card__meta">Zpracováno {{ post.date | date: "%d. %m. %Y" }}{% if post.original_date %} · původní článek z {{ post.original_date | date: "%d. %m. %Y" }}{% endif %} {% include verdict-badge.html post=post %}</p>
<div class="excerpt">{{ post.excerpt }}</div>
<a class="post-card__more" href="{{ site.baseurl }}{{ post.url }}">Číst dále →</a>
</article>
{% endunless -%}
{% endfor %}
</details>
