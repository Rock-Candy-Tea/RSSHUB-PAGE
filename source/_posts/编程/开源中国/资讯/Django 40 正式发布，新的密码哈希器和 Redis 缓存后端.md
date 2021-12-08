
---
title: 'Django 4.0 正式发布，新的密码哈希器和 Redis 缓存后端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8596'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 06:45:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8596'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Django 4.0 正式发布，4.0 版本支持 Python 3.8、3.9 和 3.10。随着 Django 4.0 的发布，Django 3.2 的主流支持已经结束。此版本主要有如下亮点：</p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新的 RedisCache 后端为使用 Redis 缓存提供了内置支持。</li> 
 <li>现在使用模板引擎呈现 Forms、Formsets 和 ErrorList ，以简化自定义的过程。</li> 
 <li>引入新的密码哈希函数 scrypt，但因为需要更多内存且依赖 OpenSSL 1.1+ ，不是默认启用项</li> 
 <li>Python 标准库的 zoneinfo 现在作为 Django 中的默认时区。</li> 
 <li>新增函数式唯一约束。</li> 
 <li>...</li> 
</ul> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">重要更新</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><code>zoneinfo</code><strong><span> </span>作为默认时区</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Django 3.2 允许使用非<span> </span><code><strong>pytz</strong></code><span> </span>时区。Django 4.0 是<span> </span><code><strong>zoneinfo</strong></code><span> </span>作为默认时区：弃用<span> </span><code><strong>pytz</strong></code><span> </span>且将在 Django 5.0 中删除它。zoneinfo 是 Python 3.9 标准库的一部分，如果你在使用 Python 3.8 ，则会自动安装 zoneinfo 包。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">注意，如果你处于非 utc（世界标准时间） 时区，且在使用 pytz normalize() 和 localalize () api，那你可能设置了TIME_ZONE ，需要审查一下代码。4.x 系列版本周期有一个过渡性的<span> </span><code>use_depreccated_pytz</code><span> </span>设置，允许从<span> </span><code><strong>pytz</strong></code><span> </span>慢慢过渡到<span> </span><code><strong>zoneinfo</strong></code>，这个设置将在 Django 5.0 中删除。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">此外，zoneinfo 作者创建的<span> </span><code>pytz_deprecation_shim</code><span> </span>包用于帮助从<span> </span><code>pytz</code><span> </span>进行迁移，这个包提供 shims 来安全地移除<span> </span><code>pytz</code>，还有一个详细的迁移指南，展示如何移动到新的<span> </span><code>zoneinfo</code><span> </span>api。渐进更新可以用 pytz_deprecation_shim和use_depreccated_pytz 这两个过渡设置。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>函数的唯一约束</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint"><code>UniqueConstraint()</code></a><span> </span>的新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2Fdev%2Fref%2Fmodels%2Fconstraints%2F%23django.db.models.UniqueConstraint.expressions"><code>*expressions</code></a><span> </span>位置参数可以在表达式和数据库函数上创建函数式唯一约束。例如：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start">from django.db import models
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
        ]</pre> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">使用该<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Foptions%2F%23django.db.models.Options.constraints" target="_blank"><code><strong>Meta.constraints</strong></code></a>选项将函数唯一约束添加到模型中 。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>增加<span> </span></strong><code><strong>scrypt</strong></code><strong><span> </span>密码哈希器</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新的<span> </span><code>scrypt</code><span> </span>密码哈希器比 PBKDF2 更安全，建议使用。但它不是默认选项，因为它需要 OpenSSL 1.1 以上版本和更多的内存。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Redis 缓存后端</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新的<code>django.core.cache.backends.redis.RedisCache</code><span> </span>缓存后端为使用 Redis 缓存提供了内置支持。此功能<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.org%2Fproject%2Fredis%2F">需要 redis-py</a> 3.0.0 或更高版本。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>基于模板的表单渲染</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">使用模板引擎渲染表单，如用于表单的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fforms%2Fapi%2F%23django.forms.Form.render" target="_blank"><code><strong>render()</strong></code></a>,<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fforms%2Fapi%2F%23django.forms.Form.get_context" target="_blank"><code><strong>get_context()</strong></code></a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fforms%2Fapi%2F%23django.forms.Form.template_name" target="_blank"><code><strong>template_name</strong></code></a>，用于表单集的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Fforms%2Fformsets%2F%23formset-rendering" target="_blank">五个渲染相关的属性和方法</a>。</p> 
<h2 style="margin-left:.6em; margin-right:0; text-align:start">次要更新项：</h2> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fadmin%2F%23module-django.contrib.admin" target="_blank"><code><strong>django.contrib.admin</strong></code></a></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><code><strong>admin/base.html</strong></code><span> </span>模板现在有一个<span> </span><code><strong>header</strong></code><span> </span>，包含管理站点标题的新模块。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fadmin%2F%23django.contrib.admin.ModelAdmin.get_formset_kwargs" target="_blank"><code><strong>ModelAdmin.get_formset_kwargs()</strong></code></a><span> </span>方法允许自定义传递给表单集构造函数的关键字参数。</li> 
 <li>侧边栏的导航有一个快速过滤器工具栏。</li> 
 <li><span style="color:#2e3033">新的上下文变量模型(包含每个模型的模型类)被添加到<span> </span><code>AdminSite.each_context()</code><span> </span>方法中。</span></li> 
 <li>新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fadmin%2F%23django.contrib.admin.ModelAdmin.search_help_text" target="_blank"><code><strong>ModelAdmin.search_help_text</strong></code></a><span> </span>属性允许为搜索框指定描述性文本</li> 
 <li>jQuery 从 3.5.1 版本升级到 3.6.0。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Ftopics%2Fauth%2F%23module-django.contrib.auth" target="_blank"><code><strong>django.contrib.auth</strong></code></a></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>PBKDF2 密码散列器的默认迭代计数从 260,000 增加到 320,000。</li> 
 <li>新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Fauth%2Fdefault%2F%23django.contrib.auth.views.LoginView.next_page" target="_blank"><code><strong>LoginView.next_page</strong></code></a><span> </span>属性和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Fauth%2Fdefault%2F%23django.contrib.auth.views.LoginView.get_default_redirect_url" target="_blank"><code><strong>get_default_redirect_url()</strong></code></a>方法允许在登录后自定义重定向。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fgis%2F%23module-django.contrib.gis" target="_blank"><code><strong>django.contrib.gis</strong></code></a></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了对 SpatiaLite 5 的支持。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fgis%2Fgdal%2F%23django.contrib.gis.gdal.GDALRaster" target="_blank"><code><strong>GDALRaster</strong></code></a><span> </span>现在允许在任何 GDAL 虚拟文件系统中创建栅格。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fpostgres%2F%23module-django.contrib.postgres" target="_blank"><code><strong>django.contrib.postgres</strong></code></a></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>PostgreSQL 后端现在支持通过服务名称进行连接。详情请参见<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdatabases%2F%23postgresql-connection-settings" target="_blank">PostgreSQL 连接配置</a>。</li> 
 <li>新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Foperations%2F%23django.contrib.postgres.operations.AddConstraintNotValid" target="_blank"><code><strong>AddConstraintNotValid</strong></code></a><span> </span>操作允许在 PostgreSQL 上创建检查约束，而无需验证所有现有行是否满足新约束。</li> 
 <li>新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Foperations%2F%23django.contrib.postgres.operations.ValidateConstraint" target="_blank"><code><strong>ValidateConstraint</strong></code></a><span> </span>操作允许验证<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Foperations%2F%23django.contrib.postgres.operations.AddConstraintNotValid" target="_blank"><code><strong>AddConstraintNotValid</strong></code></a><span> </span>在 PostgreSQL 上创建的检查约束 。</li> 
 <li>新  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Fexpressions%2F%23django.contrib.postgres.expressions.ArraySubquery" target="_blank"><code><strong>ArraySubquery()</strong></code></a><span> </span>表达式允许使用子查询在 PostgreSQL 上构建值列表。</li> 
 <li>新的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Flookups%2F%23std%3Afieldlookup-trigram_word_similar" target="_blank"><code><strong>trigram_word_similar</strong></code></a><span> </span>查找和  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Fsearch%2F%23django.contrib.postgres.search.TrigramWordDistance" target="_blank"><code><strong>TrigramWordDistance()</strong></code></a><span> </span>和<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fpostgres%2Fsearch%2F%23django.contrib.postgres.search.TrigramWordSimilarity" target="_blank"><code><strong>TrigramWordSimilarity()</strong></code></a><span> </span>表达式允许使用三元组词汇相似性（trigram word similarity）。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fstaticfiles%2F%23module-django.contrib.staticfiles" target="_blank"><code><strong>django.contrib.staticfiles</strong></code></a></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fcontrib%2Fstaticfiles%2F%23django.contrib.staticfiles.storage.ManifestStaticFilesStorage" target="_blank"><code><strong>ManifestStaticFilesStorage</strong></code></a><span> </span><span style="color:#2e3033">现在将 JavaScript 源映射引用的路径换成它们自己的散列对应路径</span>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fstaticfiles%2F%23django.contrib.staticfiles.storage.ManifestFilesMixin" target="_blank"><code><strong>ManifestFilesMixin</strong></code></a><span style="color:#0c3c26"><span> </span>和<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fcontrib%2Fstaticfiles%2F%23django.contrib.staticfiles.storage.ManifestStaticFilesStorage" target="_blank"><code><strong>ManifestStaticFilesStorage</strong></code></a><span> </span>的新参数<span> </span><span style="color:#0c4b33"><code><strong>manifest_storage</strong></code></span><span> </span>允许自定义清单文件的存储。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">缓存</h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">新的异步 API：<span> </span><code><strong>django.core.cache.backends.base.BaseCache</strong></code>开始使缓存后端异步兼容。新的异步方法都有<span> </span><code><strong>a</strong></code><span> </span>前缀的名称，例如<code><strong>aadd()</strong></code>，<code><strong>aget()</strong></code>，<code><strong>aset()</strong></code>，<span> </span><code><strong>aget_or_set()</strong></code>，或<code><strong>adelete_many()</strong></code>。</p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">以后<strong><span> </span></strong><code><strong>a</strong></code><span> </span>前缀一般会用于方法的异步变体。</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>CSRF </strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>CSRF 保护现在参考<span> </span><code><strong>Origin</strong></code><span> </span>标头（如果存在）。为此需要对<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fsettings%2F%23std%3Asetting-CSRF_TRUSTED_ORIGINS" target="_blank"><code><strong>CSRF_TRUSTED_ORIGINS</strong></code></a><span> </span>设置进行一些更改。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>国际化</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加了对马来语的支持和翻译。</li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>通用视图</strong></h3> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fclass-based-views%2Fgeneric-editing%2F%23django.views.generic.edit.DeleteView" target="_blank"><code><strong>DeleteView</strong></code></a><span> </span>现在使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fclass-based-views%2Fmixins-editing%2F%23django.views.generic.edit.FormMixin" target="_blank"><code><strong>FormMixin</strong></code></a>，允许您提供一个<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fforms%2Fapi%2F%23django.forms.Form" target="_blank"><code><strong>Form</strong></code></a><span> </span>子类，例如带有确认删除之类的复选框。</p> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>日志</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>SQL 调用中使用的数据库别名现在作为额外的上下文，与每条消息一起传递给<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Flogging%2F%23django-db-logger" target="_blank">django.db.backends</a><span> </span>记录器。</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>管理命令</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdjango-admin%2F%23django-admin-runserver" target="_blank"><code><strong>runserver</strong></code></a><span> </span>管理命令现在支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-skip-checks" target="_blank"><code><strong>--skip-checks</strong></code></a>选项。</li> 
 <li>在 PostgreSQL 上，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdjango-admin%2F%23django-admin-dbshell" target="_blank"><code><strong>dbshell</strong></code></a><span> </span>现在支持指定密码文件。</li> 
 <li>新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fhowto%2Fcustom-management-commands%2F%23django.core.management.BaseCommand.suppressed_base_arguments" target="_blank"><code><strong>BaseCommand.suppressed_base_arguments</strong></code></a>属性允许在输出中阻止不支持的命令选项。</li> 
 <li><span style="color:#2e3033">新的<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-startapp-exclude" target="_blank"><span style="color:#2e3033"><code>startapp——exclude</code></span></a><span style="color:#2e3033"><span> </span>和<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-startproject-exclude" target="_blank"><span style="color:#2e3033"><code>startproject——exclude</code></span></a><span style="color:#2e3033"><span> </span>选项允许从模板中排除目录</span></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start">模块</h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li>新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fquerysets%2F%23django.db.models.query.QuerySet.contains" target="_blank"><code><strong>QuerySet.contains(obj)</strong></code></a>方法返回查询集是否包含给定的对象，会尝试以最简单和最快的方式执行查询。</li> 
 <li>数据库函数  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fdatabase-functions%2F%23django.db.models.functions.Round" target="_blank"><code><strong>Round()</strong></code></a><span> </span>有新的<span> </span><code><strong>precision</strong></code><span> </span>参数，允许指定舍入的小数位数。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fquerysets%2F%23django.db.models.query.QuerySet.bulk_create" target="_blank"><code><strong>QuerySet.bulk_create()</strong></code></a><span> </span>现在在使用 SQLite 3.35+ 时设置对象的主键。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Ffields%2F%23django.db.models.DurationField" target="_blank"><code><strong>DurationField</strong></code></a><span> </span>现在支持在 SQLite 上乘以和除以标量值。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fquerysets%2F%23django.db.models.query.QuerySet.bulk_update" target="_blank"><code><strong>QuerySet.bulk_update()</strong></code></a><span> </span>现在返回更新后的对象数。</li> 
 <li>新的<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fexpressions%2F%23django.db.models.Expression.empty_result_set_value" target="_blank"><code><strong>Expression.empty_result_set_value</strong></code></a><span> </span>属性<span style="color:#2e3033">允许指定函数在空集上使用时返回什么值</span>。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Fquerysets%2F%23django.db.models.query.QuerySet.select_for_update" target="_blank"><code><strong>QuerySet.select_for_update()</strong></code></a>的<span> </span><code><strong>skip_locked</strong></code><span> </span>参数，现在允许在 MariaDB 10.6 以上版本使用。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmodels%2Flookups%2F%23django.db.models.Lookup" target="_blank"><code><strong>Lookup</strong></code></a>现在可以在<code><strong>QuerySet</strong></code><span> </span>注释、聚合中使用表达式，且可以直接在过滤器中使用。</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>请求和响应</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fmiddleware%2F%23django.middleware.security.SecurityMiddleware" target="_blank"><code><strong>SecurityMiddleware</strong></code></a><span> </span>现在增加了跨来源打开器策略（<span style="color:#0c4b33"><strong>Cross-Origin-Opener-Policy</strong></span>）标头的值：<code><strong>'same-origin'</strong></code>，以防止交叉来源的弹出窗口请求共享同一浏览器的上下文，使用 COOP 隔离窗口是一种针对跨域攻击的深度防御保护，尤其是像 Spectre 这样的攻击（允许外泄加载到共享浏览上下文中的数据）。</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>信号</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><span style="color:#2e3033">用于<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fsignals%2F%23django.db.models.signals.pre_migrate" target="_blank"><code><strong>pre_migrate()</strong></code></a><span style="color:#0c3c26"><span> </span>和<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fsignals%2F%23django.db.models.signals.post_migrate" target="_blank"><code><strong>post_migrate()</strong></code></a><span style="color:#2e3033"><span> </span>信号的新<span> </span><code>stdout</code><span> </span>参数，允许将输出重定向到一个类似流的对象。</span></li> 
 <li>为了在测试时正确捕获，它应该优先于 并且在发出详细输出时。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fsignals%2F%23django.db.models.signals.pre_migrate" target="_blank"><code><strong>pre_migrate()</strong></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fsignals%2F%23django.db.models.signals.post_migrate" target="_blank"><code><strong>post_migrate()</strong></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fsys.html%23sys.stdout" target="_blank"><code><strong>sys.stdout</strong></code></a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Ffunctions.html%23print" target="_blank"><code><strong>print()</strong></code></a></li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>模板</strong></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Ftemplates%2Fbuiltins%2F%23std%3Atemplatefilter-floatformat" target="_blank"><code><strong>floatformat</strong></code></a><span> </span>模板过滤器现在允许使用<span> </span><code><strong>u</strong></code><span> </span>后缀强制禁用本地化。</li> 
</ul> 
<h4 style="margin-left:.6em; margin-right:0; text-align:start"><strong>测试</strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Freleases%2F4.0%2F%23tests" target="_blank"><strong>¶</strong></a></h4> 
<ul style="margin-left:0; margin-right:0"> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Ftopics%2Ftesting%2Fadvanced%2F%23django.test.utils.setup_databases" target="_blank"><code><strong>django.test.utils.setup_databases()</strong></code></a><span> </span>的新参数<span> </span><code><strong>serialized_aliases</strong></code><span> </span> 可以决定哪些<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fsettings%2F%23std%3Asetting-DATABASES" target="_blank"><code><strong>DATABASES</strong></code></a>别名测试数据库应该将自身状态序列化，以允许使用<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Ftesting%2Foverview%2F%23test-case-serialized-rollback" target="_blank">serialized_rollback</a><span> </span>功能。</li> 
 <li>Django 测试运行器现在支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-test-buffer" target="_blank"><code><strong>--buffer</strong></code></a><span> </span>并行测试选项。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Ftopics%2Ftesting%2Fadvanced%2F%23django.test.runner.DiscoverRunner" target="_blank"><code><strong>DiscoverRunner</strong></code></a><span style="color:#2e3033"><span> </span></span>的新<span> </span><code><strong>logger</strong></code><span> </span>参数<span style="color:#2e3033">允许使用 Python 记录器进行日志记录。</span></li> 
 <li>Django 测试运行器现在支持<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-test-shuffle" target="_blank"><code><strong>--shuffle</strong></code></a><span> </span>以随机顺序执行测试的选项。</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Fref%2Fdjango-admin%2F%23cmdoption-test-parallel" target="_blank"><code><strong>test --parallel</strong></code></a><span style="color:#2e3033"><span> </span>选项现在支持<span> </span><code><strong>auto</strong></code><span> </span>值：为每个处理器核心运行一个测试进程。</span></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Ftesting%2Ftools%2F%23django.test.TestCase.captureOnCommitCallbacks" target="_blank"><code><strong>TestCase.captureOnCommitCallbacks()</strong></code></a>现在捕获执行<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fzh-hans%2F4.0%2Ftopics%2Fdb%2Ftransactions%2F%23django.db.transaction.on_commit" target="_blank"><code><strong>transaction.on_commit()</strong></code></a><span> </span>回调时添加的新回调。</li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Django 4.0 是一个超大版本更新，除了上述更新以外还包含一些功能的弃用，以及不向后兼容的更新项，完整版更新内容可在<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.djangoproject.com%2Fen%2F4.0%2Freleases%2F4.0%2F" target="_blank">更新公告</a>中查看。</p> 
<p> </p>
                                        </div>
                                      
</div>
            