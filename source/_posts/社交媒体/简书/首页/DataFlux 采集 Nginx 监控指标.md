
---
title: 'DataFlux 采集 Nginx 监控指标'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://www.jianshu.com/p/undefined'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://www.jianshu.com/p/undefined'
---

<div>   
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="960" data-height="594"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-798d2d9dfcb1ca21" data-original-width="960" data-original-height="594" data-original-format="image/jpeg" data-original-filesize="176197" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>前言</h2>
<blockquote>
<p>DataFlux是上海驻云自研发的一套大数据统一分析平台，可以通过对任何来源、类型、规模的实时数据进行监控、分析和处理，释放数据价值。</p>
<p>地址：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.dataflux.cn%2F" target="_blank">https://www.dataflux.cn/</a></p>
</blockquote>
<p>DataFlux包含五大功能模块：</p>
<ul>
<li><p>Datakit 采集器</p></li>
<li><p>Dataway 数据网关</p></li>
<li><p>DataFlux Studio 实时数据洞察平台</p></li>
<li><p>DataFlux Admin Console 管理后台</p></li>
<li><p>DataFlux.f(x) 实时数据处理开发平台</p></li>
</ul>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="764" data-height="428"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-3a8001dfb8f6baa4" data-original-width="764" data-original-height="428" data-original-format="image/png" data-original-filesize="86935" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>面向企业提供全场景的数据洞察分析能力， 具有实时性、灵活性、易扩展、易部署等特点。</p>
<p>Nginx作为常用的Web容器之一，很多运维（开发）小伙伴经常使用它来搭建Web网站服务器。今天跟大家分享一个监控SAAS平台，只需要简单配置，就可以实现站点以及业务监控——使用DataFlux采集Nginx性能指标并分析展示。</p>
<p>不过部分功能是需要收费，目前工作中免费的部分足够使用。感兴趣的小伙伴可以去官网了解下。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="611"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-d3f553ab02e7d6f2" data-original-width="1080" data-original-height="611" data-original-format="image/png" data-original-filesize="173467" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption">image</div>
</div>
<p><strong>使用场景</strong></p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="511"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-75b709b717d34f5e" data-original-width="1080" data-original-height="511" data-original-format="image/png" data-original-filesize="100919" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h2>安装流程</h2>
<h1>安装DataKit</h1>
<p>PS：以Linux系统为例</p>
<p>第一步：执行安装命令</p>
<p>DataKit 安装命令：</p>
<pre><code>DK_FTDATAWAY=[你的 DataWay 网关地址] bash -c "$(curl https://static.dataflux.cn/datakit/install.sh)"
</code></pre>
<p>补充安装命令中的 DataWay 网关地址，然后复制安装命令到主机上执行即可。</p>
<p>例如：如果的 DataWay 网关地址 IP 为 1.2.3.4，端口为 9528(9528为默认端口)，则网关地址为 <a href="https://links.jianshu.com/go?to=http%3A%2F%2F1.2.3.4%3A9528%2Fv1%2Fwrite%2Fmetrics" target="_blank">http://1.2.3.4:9528/v1/write/metrics</a>，安装命令为：</p>
<pre><code>DK_FTDATAWAY=http://1.2.3.4:9528/v1/write/metrics bash -c "$(curl https://static.dataflux.cn/datakit/install.sh)"
</code></pre>
<p>安装完成后，DataKit 默认会自动运行，并且会在终端中提示 DataKit 的状态管理命令</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="640" data-height="239"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-f899a2c92795a9c1" data-original-width="640" data-original-height="239" data-original-format="image/jpeg" data-original-filesize="15332" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>Nginx 监控指标采集</p>
<p>按需采集各种版本的 nginx 指标，并上报到 DataFlux 中。</p>
<ul>
<li><p>nginx （基本状态信息）</p></li>
<li><p>nginx_plus（所有状态信息）</p></li>
<li><p>nginx_plus_api （API文档）</p></li>
<li><p>nginx_upstream_check （nginx_upstream_check_module 模块信息）</p></li>
<li><p>nginx_vts（nginx-module-vts 模块信息）</p></li>
</ul>
<p>前置条件</p>
<ul>
<li><p>已安装 DataKit（DataKit 安装文档）</p></li>
<li><p>开启 nginx 的 ngx_http_stub_status_module 模块。</p></li>
</ul>
<p>配置</p>
<p>打开 DataKit 采集源配置文件夹（默认路径为 DataKit 安装目录的 conf.d 文件夹），找到 nginx 文件夹，打开里面的 nginx.conf。</p>
<p>修改配置文件如图所示。</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="639" data-height="261"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-113ee9c15e8d0f1d" data-original-width="639" data-original-height="261" data-original-format="image/jpeg" data-original-filesize="36554" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>配置好后，重启 DataKit 即可生效。</p>
<h1>验证数据上报</h1>
<p>完成数据采集操作后，我们需要验证数据是否采集成功并且上报到DataWay，以便后续能正常进行数据分析及展示</p>
<p>操作步骤：登录DataFlux——数据管理——指标浏览——验证数据是否采集成功</p>
<p>Nginx 指标：</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="192"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-d36b3cdbf74b54c0" data-original-width="1080" data-original-height="192" data-original-format="image/jpeg" data-original-filesize="16917" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h1>使用DataFlux实现数据洞察</h1>
<p>根据获取到的指标项进行数据洞察设计，例如：</p>
<p>Nginx 监控视图</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="640" data-height="310"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-aa3654789ce58336" data-original-width="640" data-original-height="310" data-original-format="image/jpeg" data-original-filesize="22513" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>​</p>
<p>DataFlux基于自研的DataKit数据（采集器）目前已经可以对接超过200种数据协议，包括：云端数据采集、应用数据采集、日志数据采集、时序数据上报、常用数据库的数据汇聚，帮助企业实现最便捷的IT 统一监控。</p>
<p>展示部分使用用户</p>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1080" data-height="383"><img data-original-src="//upload-images.jianshu.io/upload_images/16753854-41c24c2fa417c899" data-original-width="1080" data-original-height="383" data-original-format="image/png" data-original-filesize="187475" src="https://www.jianshu.com/p/undefined" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<ul>
<li><em>更多测试技术分享、学习资源以及一些其他福利可关注公众号：【Coding测试】获取：</em></li>
</ul>
  
</div>
            