---
layout: home
title: BC Daily Digest
---

# Přehled novinek ze světa programování v AL

{%- comment -%}
Hranice "nového" článku: původní článek z posledních 30 dní (30*24*3600 s).
Sekce se řadí podle data zpracování (pořadí site.posts), jen se rozdělí
na nové a archivní, aby čerstvý obsah nezapadl mezi dozpracovaný archiv.
Pozor: HTML níže musí být na sloupci 0 – odsazení o 4+ mezery by kramdown
vykreslil jako blok kódu místo HTML.
{%- endcomment -%}
{% assign now_ts = 'now' | date: '%s' | plus: 0 %}
{% assign cutoff_ts = now_ts | minus: 2592000 %}

## Nové články

{% assign found_new = false -%}
{% for post in site.posts -%}
{%- assign is_new = false -%}
{%- if post.original_date -%}
{%- assign ots = post.original_date | date: '%s' | plus: 0 -%}
{%- if ots >= cutoff_ts %}{% assign is_new = true %}{% endif -%}
{%- endif -%}
{%- if is_new -%}
{%- assign found_new = true %}
<article>
<h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
<p>Zpracováno {{ post.date | date: "%d. %m. %Y" }}{% if post.original_date %} · původní článek z {{ post.original_date | date: "%d. %m. %Y" }}{% endif %}</p>
<div class="excerpt">{{ post.excerpt }}</div>
<a href="{{ site.baseurl }}{{ post.url }}">Číst dále...</a>
</article>
{% endif -%}
{% endfor -%}
{% unless found_new %}<p><em>Zatím žádné nové články.</em></p>{% endunless %}

<details class="archive">
<summary>Z archivu</summary>
{% for post in site.posts -%}
{%- assign is_new = false -%}
{%- if post.original_date -%}
{%- assign ots = post.original_date | date: '%s' | plus: 0 -%}
{%- if ots >= cutoff_ts %}{% assign is_new = true %}{% endif -%}
{%- endif -%}
{%- unless is_new %}
<article>
<h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
<p>Zpracováno {{ post.date | date: "%d. %m. %Y" }}{% if post.original_date %} · původní článek z {{ post.original_date | date: "%d. %m. %Y" }}{% endif %}</p>
<div class="excerpt">{{ post.excerpt }}</div>
<a href="{{ site.baseurl }}{{ post.url }}">Číst dále...</a>
</article>
{% endunless -%}
{% endfor %}
</details>
