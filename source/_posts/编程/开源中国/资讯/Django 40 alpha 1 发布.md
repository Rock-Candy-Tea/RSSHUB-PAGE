
---
title: 'Django 4.0 alpha 1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8879'
author: 开源中国
comments: false
date: Wed, 22 Sep 2021 23:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8879'
---

<div>   
<div class="content">
                                                                                            <p>Django 4.0 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fweblog%2F2021%2Fsep%2F21%2Fdjango-40-alpha-1-released%2F" target="_blank">发布</a>了首个 alpha 版本，标志着已进入功能冻结阶段。开发团队称计划在未来一个月内发布 beta 测试版，然后在测试版发布一个月后推出 RC 候选版。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fdownload%2F" target="_blank">https://www.djangoproject.com/download/</a></p> 
<p>Django 4.0 主要变化</p> 
<p><strong>使用<code><span>zoneinfo</span></code>作为默认时区实现</strong></p> 
<p>Python 标准库<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html%23module-zoneinfo" target="_blank"><code><span>zoneinfo</span></code></a><span style="background-color:#ffffff; color:#0c3c26">现在是 Django 的默认时区实现。其中</span>对<code><span><span><span>pytz</span></span></span></code>的支持已弃用，并将在 Django 5.0 中删除。</p> 
<p>根据开发团队的介绍，转向<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html%23module-zoneinfo" target="_blank"><code><span>zoneinfo</span></code></a>后，<span style="background-color:#ffffff; color:#0c3c26">当前时区的选择、将日期时间实例转换为表单和模板中的当前时区以及对 UTC 中的<span> </span>aware datetimes </span><span style="background-color:#ffffff; color:#0c3c26">的操作不受影响。</span></p> 
<p><strong>函数式的唯一约束</strong></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint" target="_blank"><code><span>UniqueConstraint()</span></code></a>的新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint.expressions" target="_blank"><code><span>*expressions</span></code></a>positional 参数可以在表达式和数据库函数上创建函数式唯一约束。例如：</p> 
<pre><code class="language-python">from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower


class MyModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        indexes = [
            UniqueConstraint(
                Lower('first_name'),
                Lower('last_name').desc(),
                name='first_last_name_unique',
            ),
        ]</code></pre> 
<p><strong>增加<span><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span><span><span>scrypt</span></span></span></code>密码哈希器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<p>新的<span><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><code><span><span><span>scrypt</span></span></span></code>密码哈希器</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>比 PBKDF2 更安全，建议使用。但它不是默认选项，因为它需要 OpenSSL 1.1 以上版本和更多的内存。</p> 
<p><strong><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span style="color:#0c3c26"><span>Redis 缓存后端</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
<div style="text-align:start"> 
 <p style="margin-left:0px; margin-right:0px"><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>新的<code><span><span><span>django.core.cache.backends.redis.RedisCache</span></span></span></code>缓存后端为使用 Redis 缓存提供了内置支持。此功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Fredis%2F" target="_blank">需要 redis-py</a> 3.0.0 或更高版本。有关更多详细信息，请查看有关在 Django 中使用 Redis 进行缓存的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Ftopics%2Fcache%2F%23redis" target="_blank">文档</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p style="margin-left:0px; margin-right:0px"><strong><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><span style="color:#0c3c26"><span>基于模板的表单渲染</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></p> 
</div> 
<div style="text-align:start"> 
 <p style="margin-left:0px; margin-right:0px"><span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>为了提高定制<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fforms%2Fapi%2F%23django.forms.Form" target="_blank"><code><span><span><span>Forms</span></span></span></code></a>、</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Ftopics%2Fforms%2Fformsets%2F" target="_blank"><span>Formsets</span></a> <span><span style="color:#0c3c26"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fforms%2Fapi%2F%23django.forms.ErrorList" target="_blank"><code><span><span><span>ErrorList</span></span></span></code></a>，开发者现在正在使用的模板引擎进行渲染。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
 <p style="margin-left:0px; margin-right:0px">详细更新说明查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Freleases%2F4.0%2F" target="_blank"> release notes</a>。</p> 
</div>
                                        </div>
                                      
</div>
            