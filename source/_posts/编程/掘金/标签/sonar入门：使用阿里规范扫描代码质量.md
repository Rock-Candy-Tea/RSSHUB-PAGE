
---
title: 'sonar入门：使用阿里规范扫描代码质量'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29e0e9e178b848df9cd88395e2b82431~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 16:27:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29e0e9e178b848df9cd88395e2b82431~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto;border:3px solid rgba(62,175,124,.2)&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-weight:700;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:6px;border:2px solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c&#125;.markdown-body a:active,.markdown-body a:hover&#123;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a:before&#123;content:"⇲"&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(62,175,124,.2)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:.5rem solid;border-color:#42b983;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none&#125;.markdown-body ul li:before&#123;content:"•";margin-right:4px;color:#3eaf7c&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>这是我参与 8 月更文挑战的第 25 天，活动详情查看： <a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
</blockquote>
<p>检测java代码时 有两种方法 </p>
<ul>
<li>使用sonar-scanner</li>
<li>SonarLint+maven</li>
</ul>
<p>SonarLint+maven可能对于代码耦合度比较大，而且更复杂，所以楼主推荐sonar-scanner方式 。</p>
<p>废话不多说 安排！</p>
<h2 data-id="heading-0">1.使用sonar-scanner扫描</h2>
<h3 data-id="heading-1">1.打包</h3>
<p>打包java项目，这里不多说。</p>
<h3 data-id="heading-2">2.新家配置文件</h3>
<p>在src路径下建立sonar-project.properties。配置文件如下。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29e0e9e178b848df9cd88395e2b82431~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"># 项目名称
sonar.projectKey=systemportal
sonar.projectName=systemportal
sonar.projectVersion=1.0

#代码路径
sonar.sources=./src

# class路径
sonar.java.binaries=./target/classes

# 语言格式
sonar.language=java
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">3.执行扫描</h3>
<p>进入sonar-project.properties路径通过cmd执行。</p>
<pre><code class="copyable">sonar-scanner
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下字样为执行成功。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04cedd321c894224928c9860333b60ab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
进入127.0.0.1:9000，可以看到bug数啦。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cabe9272af444068aec7ae3e0bb5039~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2.SonarLint+maven扫描</h2>
<h3 data-id="heading-5"> 1.idea安装SonarLint插件</h3>
<p>打开File->Settings->Plugins,搜索SonarLint插件，点击安装。安装后重启idea，如果安装失败，在网上下载插件，丢到idea安装目录的plugins文件夹中。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f2b504b7e924f76ae9ad9834df70bdc~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">2.配置SonarLint</h3>
<p>配置SonarLint General Settings。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9de57ad9648a4f3d8fe506c22e3d871e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>地址为安装sonarqube地址 地址一定要带 http://</p>
</blockquote>
<p>点击next后可以选择验证类型填写安装时配置的账号密码</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2bbc334a20b4e0390c5abeb17d5075c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">3.配置SonarLint Project Settings</h3>
<p>选择刚才配置的规则</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa903e7332634c2390abab9eda9606fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">4.配置springboot</h3>
<p>pom.xml文件中添加plugin。</p>
<pre><code class="copyable"><plugin>
    <groupId>org.sonarsource.scanner.maven</groupId>
    <artifactId>sonar-maven-plugin</artifactId>
    <version>3.4.0.905</version>
</plugin>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.打包扫描</h3>
<pre><code class="copyable">mvn clean compile install
mvn sonar:sonar -Dsonar.host.url=http://xxx.xxx.xx.xx:9000  #上文配置的地址
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">6.查看</h3>
<p>执行完命令后回到SonarLint Project Settings，点击search in list 选择项目。
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69be25fdf7a24b2eb0e9add1a4c86128~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后就可以查看代码质量了。可以查看单个文件也可以查看文件夹。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/95ad6005ad374b748a8901e97d07493c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
检测的结果也可以在sonarqube中查看，访问上文配置的地址即可，看完后就可以有理由的喷一喷小弟了。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66c990f16a5e4bf0b438082ad3a8dcb6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">3.使用p3c规则</h2>
<blockquote>
<p>书接上文，还是不建议使用自带规则。字楼楼主选择了阿里出品的p3c。</p>
</blockquote>
<h3 data-id="heading-12">1.下载sonar-p3c-pmd</h3>
<p>sonarqube的版本号与sonar-p3c-pmd是对应的，所以需要选择好版本，楼主版本为7.6，否则会还会报es连接不上的错误。
地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frhinoceros%2Fsonar-p3c-pmd%2Freleases%2Ftag%2Fpmd-3.2.0-beta-with-p3c1.3.6-pmd6.10.0" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rhinoceros/sonar-p3c-pmd/releases/tag/pmd-3.2.0-beta-with-p3c1.3.6-pmd6.10.0" ref="nofollow noopener noreferrer">github.com/rhinoceros/…</a>。</p>
<h3 data-id="heading-13">2.选择版本</h3>
<p>选择合适的jar包。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9919a98c6ab4b0ca2d322602b4053e5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">3.修改配置</h3>
<p>删除之前pmd文件，放于sonarqube-7.6\extensions\plugins中，重启服务。</p>
<h3 data-id="heading-15">3.创建p3c规则</h3>
<p>新增配置类别。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f920abcdbca145b69778eac2ddf7c7f6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
激活配置规则
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/704fd5c21c584e48bcfddc71dbeb7fab~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
选择资源库中的pmd(之前导入的p3c-pdm) 然后选择包中的规则激活即可，楼主这里只激活了p3c的51条。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff6ba001275249e683b1af3b4b12d426~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
设为默认即可</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6b9dc7cae8a4295b9eb2e377ac25581~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
然后再次扫描即就是使用了新规范扫描了，是不是清爽了很多呢。</p></div>  
</div>
            