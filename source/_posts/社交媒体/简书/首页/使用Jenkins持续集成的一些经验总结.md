
---
title: '使用Jenkins持续集成的一些经验总结'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://upload-images.jianshu.io/upload_images/3512339-190be59142fff219.png'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://upload-images.jianshu.io/upload_images/3512339-190be59142fff219.png'
---

<div>   
<blockquote>
<p>Jenkins version: 2.263.4 LTS<br>
持续更新中...</p>
</blockquote>
<hr>
<h2>Performance插件兼容性问题</h2>
<p>自由风格项目中，有使用<code>Performance</code>插件收集构建产物，但是截至到目前最新版本（Jenkins v2.298，Performance：v3.19），此插件和Jenkins都存在有<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fissues.jenkins.io%2Fbrowse%2FJENKINS-65109" target="_blank">兼容性问题</a>，会导致项目配置页面table, div错位，而导致无法保存配置，这个问题已经存在了好长时间了（至少半年），插件作者一直没有修复，目前在项目中要想使用这个插件，有以下三种解决办法：</p>
<ol>
<li>将自由风格项目切换为流水线风格；</li>
<li>服务器上手动修改项目的config.xml文件以达到保存配置的效果；</li>
<li>Jenkins版本降级，经过测试，此插件在v2.263.4 LTS上可以正常使用，降级前做好备份工作，以及考虑其他插件的兼容性问题。</li>
</ol>
<h2>修改Jenkins 安全策略（CSP）</h2>
<p>场景：借助<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fplugins.jenkins.io%2Frobot" target="_blank">Robot Framework Plugin</a>，可将Robot Framework项目更好的集成到Jenkins中，但是直接在Jenkins 项目中点击预览测试报告，会出现<code>Opening Robot Framework log failed</code>的错误，这是由于Jenkins为了避免受到恶意HTML/JS文件的攻击，会默认将安全策略CSP设置为：</p>
<pre><code>sandbox; default-src 'none'; img-src 'self'; style-src 'self';
</code></pre>
<p>在此配置下，只允许加载Jenkins服务器上托管的CSS文件和图片文件。解决办法需要借助Startup Trigger和Groovy plugin两个插件，具体步骤如下：</p>
<ol>
<li>Jenkins中新建一个Job，该Job专用Jenkins启动时执行的配置命令；</li>
<li>在“构建触发器”模块，选择“Build when job nodes start”选项，Restricted node Label保持空白，Quiet period设置为0；</li>
<li>在“构建”模块，选择“Execute system Groovy ”，执行如下Groovy命令:</li>
</ol>
<pre><code>System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
</code></pre>
<ol start="4">
<li>重启Jenkins服务器进行测试，会发现等待所有节点连接成功后此项目会立即自动触发构建。再去触发Robot项目构建，等待完成后点击访问测试报告页面，会发现已经可以正常访问了；</li>
</ol>
<h3>自定义Jenkins相对访问路径</h3>
<p>场景： nginx为Jenkins做目录代理，同时站点下还代理了很多其他的应用，这里需要自定义Jenkins相对访问路径。<br>
本机访问Jenkins的路径为：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A29908" target="_blank">http://localhost:29908</a>，需要改为：<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A29908%2Fjenkins" target="_blank">http://localhost:29908/jenkins</a>, 方法如下：</p>
<ol>
<li><p>在Jenkins安装根目录下找到 jenkins.xml文件；</p></li>
<li><p>找到service节点下的arguements子节点，并在最后面添加--prefix参数：<br>
--prefix="/jenkins"，其中 /jenkins 是自定义的访问路径;</p></li>
<li><p>重启Jenkins服务，此时本机已经可以通过<a href="https://links.jianshu.com/go?to=http%3A%2F%2Flocalhost%3A29908%2Fjenkins" target="_blank">http://localhost:29908/jenkins</a>进行访问;</p></li>
<li><p>测试目录代理访问;</p></li>
</ol>
<p>注意：如果在目录代理之前，子节点和主节点之间就已经通过JNLP的方式连接好了，则需要找到子节点根目录下的<code>jenkins-slave.xml</code>文件，将service.arguements节点<code>-jnlpUrl</code>参数值修改为正确的值。</p>
<h3>git clone失败 : Killed by signal 15</h3>
<p></p>
<p></p>
场景：jenkins项目clone代码时，出现任务被kill掉的情况，导致出现以下错误信息：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1154" data-height="387"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-190be59142fff219.png" data-original-width="1154" data-original-height="387" data-original-format="image/png" data-original-filesize="38140" src="https://upload-images.jianshu.io/upload_images/3512339-190be59142fff219.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p></p>
<p></p>
通过查看控制台的输出日志，可以看出原因是因为超时了。如果在限制时间内代码都没有clone完成，那么就任务就会被强制杀死：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="970" data-height="247"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-7f0cf6c84ba34120.png" data-original-width="970" data-original-height="247" data-original-format="image/png" data-original-filesize="75862" src="https://upload-images.jianshu.io/upload_images/3512339-7f0cf6c84ba34120.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p></p>
<p></p>
解决方法：当所需要clone的版本库过大或服务器网速较差时，clone的时间会超过默认的10分钟。因此需要修改clone的超时时间。设置方法如下：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1155" data-height="756"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-0f163b896b2e6722.png" data-original-width="1155" data-original-height="756" data-original-format="image/png" data-original-filesize="72648" src="https://upload-images.jianshu.io/upload_images/3512339-0f163b896b2e6722.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3>Jenkins:Build step 'Execute Windows batch command' marked build as failure</h3>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="569" data-height="282"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-6c7ad0948431cde8.png" data-original-width="569" data-original-height="282" data-original-format="image/png" data-original-filesize="12309" src="https://upload-images.jianshu.io/upload_images/3512339-6c7ad0948431cde8.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>场景：使用Jenkins定时跑接口测试用例，明明所有的用例都执行成功了，但是还是会触发执行失败时的邮件通知，查看Jenkins控制台日志，发现是由于上面截图的原因导致的。</p>
<p>解决方法：在bat脚本(shell同样适用)最后一行加上exit 0，表示正常运行程序并退出程序。</p>
<hr>
<h3>Jenkins运行在Tomcat容器中，替换jar包的方法</h3>
<p>背景：jenkins.war中引用的<code>commons-fileupload-1.3.1-jenkins-2.jar</code>被扫出来有安全隐患，需要替换到最新的1.4版本，因为扫描的时候是根据版本来的，如果直接采用覆盖并重命名的方法，还是会被扫出来，目前采取的方法是创建软连接。</p>
<ol>
<li>先下载最新的<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fcommons.apache.org%2Fproper%2Fcommons-fileupload%2Fdownload_fileupload.cgi" target="_blank">commons-fileupload-1.4.jar</a>
</li>
<li>创建软链接(管理员权限)，Linux系统下同理。</li>
</ol>
<pre><code>mklink webapps\jenkins\WEB-INF\lib\commons-fileupload-1.3.1-jenkins-2.jar  webapps\jenkins\WEB-INF\lib\commons-fileupload-1.4.jar
</code></pre>
<ol start="3">
<li>把旧的commons-fileupload-1.3.1-jenkins-2.jar删除</li>
<li>重启tomcat</li>
</ol>
<hr>
<h3>Windows节点机无法运行jnlp文件</h3>
<p>在节点机双击jnlp文件没有反应时，可以尝试用命令行方式运行此文件，cmd进入jnlp文件目录下，运行<code>javaws slave-agent.jnlp</code>，可以查看具体的错误提示，如下：</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="717" data-height="361"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-fc4afe74b692c47f.png" data-original-width="717" data-original-height="361" data-original-format="image/png" data-original-filesize="103371" src="https://upload-images.jianshu.io/upload_images/3512339-fc4afe74b692c47f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<p>上图中这种情况，只需要修改下java安全配置即可解决，其他情况再具体分析。</p>
<hr>
<h3>关闭CSRF防护</h3>
<p>Jenkins v2.204.6之前的版本，要想关闭CSRF防护，只需要在全局安全配置中禁用相关配置即可，但是较高版本的 Jenkins 默认均开启CSRF防护且删除了禁用的入口。要想禁用CSRF防护，只能通过配置参数的方式。<br>
Jenkins若是跑在Tomcat下，只需在tomcat启动脚本中加入配置如下：</p>
<pre><code>-Dhudson.security.csrf.GlobalCrumbIssuerConfiguration.DISABLE_CSRF_PROTECTION=true
</code></pre>
<p>若是以jar包形式部署的，只需在启动时加上配置参数即可。</p>
<hr>
<h3>修改 JVM 的内存配置</h3>
<p>无论是以 Jdk Jar 方式运行Jenkins，还是将 War 包放在 Tomcat等容器下运行，都会存在一个问题：默认 JVM 内存分配太少，这导致启动或者运行一段时间后内存溢出报错 java.lang.OutOfMemoryError: PermGen spac。所以，需要在启动前修改配置文件中的JVM 内存配置。</p>
<pre><code> set JAVA_OPTS=
 -server 
 -Xms5000M 
 -Xmx5000M  
 -Xss512k 
 -XX:+AggressiveOpts 
 -XX:+UseBiasedLocking 
 -XX:PermSize=256M 
 -XX:MaxPermSize=512M 
 -XX:+DisableExplicitGC 
 -XX:MaxTenuringThreshold=31 
 -XX:+UseConcMarkSweepGC 
 -XX:+UseParNewGC  
 -XX:+CMSParallelRemarkEnabled 
 -XX:+UseCMSCompactAtFullCollection 
 -XX:LargePageSizeInBytes=128m  
 -XX:+UseFastAccessorMethods 
 -XX:+UseCMSInitiatingOccupancyOnly 
 -Djava.awt.headless=true
</code></pre>
<p>这里的几个 JVM 参数含义如下：<br>
-Xms: 使用的最小堆内存大小<br>
-Xmx: 使用的最大堆内存大小<br>
-XX:PermSize: 内存的永久保存区域大小<br>
-XX:MaxPermSize: 最大内存的永久保存区域大小这几个参数也不是配置越大越好，具体要根据所在机器实际内存和使用大小配置。</p>
<hr>
<h3>配置优化减少磁盘空间占用</h3>
<p>Job 构建历史较多时，如果没有配置好清理策略的话，会导致占用大量磁盘空间，最终可能会因磁盘空间不够而导致构建失败。并且在加载项目配置时，Jenkins也需要花费时间分析历史构建记录，页面加载的耗时会相应的增加。</p>
<h5>丢弃旧的构建配置</h5>
<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="979" data-height="286"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-73dd51d4465f5ec1.png" data-original-width="979" data-original-height="286" data-original-format="image/png" data-original-filesize="18675" src="https://upload-images.jianshu.io/upload_images/3512339-73dd51d4465f5ec1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<p>如上图，配置最大保持 2 天之内的构建，如果超过 2 天的构建，则会在Job 执行前被清理掉，同时配置了最大保持构建数量为 30 个，意思就是如果 2 天内构建次数如果超过 30 次，则最多保留最近执行的 30 个构建。</p>
<h5>使用Disk Uasge插件</h5>
<p>不建议，使用此插件的过程中，发现可能会导致服务器卡顿。</p>
<h5>定时清理tomcat日志</h5>
<p>默认情况下，tomcat每天都会生成新的日志文件，且某些情况下，产生的日志文件体积会非常大，如果长期不清理，日志文件会越来越多，占用很多磁盘空间。</p>
<p></p>
<p></p>
目前的处理方法是在Jenkins新建了一个定时任务，专门用来删除tomcat产生的日志文件。<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="752" data-height="196"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-a4521ec1c7222a57.png" data-original-width="752" data-original-height="196" data-original-format="image/png" data-original-filesize="17360" src="https://upload-images.jianshu.io/upload_images/3512339-a4521ec1c7222a57.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<hr>
<h3>设置构建超时时间</h3>
<p></p>
<p></p>
有些 Job 在执行构建时，由于某些原因导致构建挂起，耗时比较长，而这些长时间挂起的 Job 会导致 Jenkins 内存占用比较大，性能下降，严重的会直接导致 Jenkins 挂掉。所以，我们需要设置构建超时时间来预防这种事情发生，一旦超过一定的时间，要让 Job 自动停止掉，如下：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="886" data-height="512"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-b2f1458e8b2afe02.png" data-original-width="886" data-original-height="512" data-original-format="image/png" data-original-filesize="33810" src="https://upload-images.jianshu.io/upload_images/3512339-b2f1458e8b2afe02.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>设置全局属性</h3>
<p></p>
<p></p>
适当设置全局属性，可以避免在pipeline中重复写死一些固定值，例如输出日志地址、接口请求地址等等，而且当固定值需要修改时，只需要修改一次即可，不用去每个文件里面修改，方便维护。设置入口为： 系统管理 -> 系统配置-> 全局属性-> Environment variables ，如下图：<div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="733" data-height="306"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-73bc217f1cdd068f.png" data-original-width="733" data-original-height="306" data-original-format="image/png" data-original-filesize="35393" src="https://upload-images.jianshu.io/upload_images/3512339-73bc217f1cdd068f.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div>
<h3>统一管理脚本</h3>
<p>需要安装<code>Managed script</code> 插件，该插件是为了在管理文件时创建 Script 脚本文件，然后在 Job 中配置直接使用，方便脚本的统一管理和维护。插件安装完成后，进入“系统管理” —> “Managed files” ，点击 “Add a new Config” ，并选择 “Groovy file” 类型，创建一个新的 Groovy 脚本文件，然后输入我们要执行的脚本代码，如下：<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="636" data-height="311"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-7f72cb9642d0441e.png" data-original-width="636" data-original-height="311" data-original-format="image/png" data-original-filesize="42025" src="https://upload-images.jianshu.io/upload_images/3512339-7f72cb9642d0441e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<p>创建完毕后，我们在 Job 中构建处选择 “Execute managed script” 就可以使用这些脚本了。</p>
<hr>
<h3>轻量备份</h3>
<p>使用<code>ThinBackup</code> 插件，允许我们对Jenkins配置信息进行全量或增量备份，由于插件不会保存构建历史和构建工件，所备份过程更为快捷，并且无需关闭Jenkins服务器。</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="1172" data-height="679"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-20e91927d41dd62e.png" data-original-width="1172" data-original-height="679" data-original-format="image/png" data-original-filesize="52071" src="https://upload-images.jianshu.io/upload_images/3512339-20e91927d41dd62e.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<p>还原备份：<br>
</p><div class="image-package">
<div class="image-container">
<div class="image-container-fill"></div>
<div class="image-view" data-width="720" data-height="336"><img data-original-src="//upload-images.jianshu.io/upload_images/3512339-110adfdd9ef211d1.png" data-original-width="720" data-original-height="336" data-original-format="image/png" data-original-filesize="20221" src="https://upload-images.jianshu.io/upload_images/3512339-110adfdd9ef211d1.png" referrerpolicy="no-referrer"></div>
</div>
<div class="image-caption"></div>
</div><p></p>
<hr>
  
</div>
            