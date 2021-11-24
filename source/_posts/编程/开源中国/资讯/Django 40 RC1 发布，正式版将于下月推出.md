
---
title: 'Django 4.0 RC1 发布，正式版将于下月推出'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7694'
author: 开源中国
comments: false
date: Wed, 24 Nov 2021 07:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7694'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Django 4.0 首个 RC 版本已发布。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fweblog%2F2021%2Fnov%2F22%2Fdjango-40-rc1%2F" target="_blank">发布公告写道</a>，如果未来两周没有发现无法解决的重大错误，正式版将于 12 月 6 日左右推出。若有延迟会通过开发者邮件列表进行通知。</p> 
<p>下载地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.djangoproject.com%2Fdownload%2F" target="_blank">https://www.djangoproject.com/download/</a></p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Freleases%2F4.0%2F" target="_blank">Django 4.0 主要变化</a></p> 
<ul> 
 <li>默认时区实现 zoneinfo</li> 
 <li>支持 Python 3.8、3.9 和 3.10</li> 
 <li>Django 3.2.x 系列是支持 Python 3.6 和 3.7 的最后版本</li> 
 <li>引入新密码哈希函数 scrypt，但因为需要更多内存和 OpenSSL 1.1+ 没有默认启用</li> 
 <li>Redis 缓存后端</li> 
 <li>……</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>使用<code>zoneinfo</code>作为默认时区实现</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Python 标准库<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html%23module-zoneinfo" target="_blank"><code>zoneinfo</code></a><span style="background-color:#ffffff">现在是 Django 的默认时区实现。其中</span>对<code>pytz</code>的支持已弃用，并将在 Django 5.0 中删除。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">根据开发团队的介绍，转向<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fzoneinfo.html%23module-zoneinfo" target="_blank"><code>zoneinfo</code></a>后，<span style="background-color:#ffffff">当前时区的选择、将日期时间实例转换为表单和模板中的当前时区以及对 UTC 中的 aware datetimes </span><span style="background-color:#ffffff">的操作不受影响。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>函数式的唯一约束</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint" target="_blank"><code>UniqueConstraint()</code></a>的新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint.expressions" target="_blank"><code>*expressions</code></a>positional 参数可以在表达式和数据库函数上创建函数式唯一约束。例如：</p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-python"><span style="color:#d73a49">from</span> django.db <span style="color:#d73a49">import</span> models
<span style="color:#d73a49">from</span> django.db.models <span style="color:#d73a49">import</span> UniqueConstraint
<span style="color:#d73a49">from</span> django.db.models.functions <span style="color:#d73a49">import</span> Lower


<span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">MyModel</span><span>(models.Model)</span>:</span>
    first_name = models.CharField(max_length=<span>255</span>)
    last_name = models.CharField(max_length=<span>255</span>)

    <span><span style="color:#d73a49">class</span> <span style="color:#6f42c1">Meta</span>:</span>
        indexes = [
            UniqueConstraint(
                Lower(<span style="color:#032f62">'first_name'</span>),
                Lower(<span style="color:#032f62">'last_name'</span>).desc(),
                name=<span style="color:#032f62">'first_last_name_unique'</span>,
            ),
        ]</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>增加<span style="background-color:#ffffff"><code>scrypt</code>密码哈希器</span></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新的<span style="background-color:#ffffff"><code>scrypt</code>密码哈希器</span>比 PBKDF2 更安全，建议使用。但它不是默认选项，因为它需要 OpenSSL 1.1 以上版本和更多的内存。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong><span style="background-color:#ffffff">Redis 缓存后端</span></strong></p> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff">新的<code>django.core.cache.backends.redis.RedisCache</code>缓存后端为使用 Redis 缓存提供了内置支持。此功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Fredis%2F" target="_blank">需要 redis-py</a> 3.0.0 或更高版本。有关更多详细信息，请查看有关在 Django 中使用 Redis 进行缓存的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Ftopics%2Fcache%2F%23redis" target="_blank">文档</a>。</span></p> 
 <p style="margin-left:0; margin-right:0"><strong><span style="background-color:#ffffff">基于模板的表单渲染</span></strong></p> 
</div> 
<div style="text-align:start"> 
 <p style="margin-left:0; margin-right:0"><span style="background-color:#ffffff">为了提高定制<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fforms%2Fapi%2F%23django.forms.Form" target="_blank"><code>Forms</code></a>、</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Ftopics%2Fforms%2Fformsets%2F" target="_blank">Formsets</a> <span style="background-color:#ffffff">和<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fforms%2Fapi%2F%23django.forms.ErrorList" target="_blank"><code>ErrorList</code></a>，开发者现在正在使用的模板引擎进行渲染。</span></p> 
</div>
                                        </div>
                                      
</div>
            