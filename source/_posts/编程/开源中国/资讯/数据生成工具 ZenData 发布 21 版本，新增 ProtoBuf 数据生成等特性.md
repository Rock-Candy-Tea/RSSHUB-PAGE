
---
title: '数据生成工具 ZenData 发布 2.1 版本，新增 ProtoBuf 数据生成等特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.zendata.cn/file.php?f=202104/f_abeb734e4373e96b58ec924c7bcba7d7&t=png&o=&s=&v=1615794273'
author: 开源中国
comments: false
date: Tue, 20 Apr 2021 14:38:00 GMT
thumbnail: 'https://www.zendata.cn/file.php?f=202104/f_abeb734e4373e96b58ec924c7bcba7d7&t=png&o=&s=&v=1615794273'
---

<div>   
<div class="content">
                                                                    
                                                        <p>ZenData2.1版本发布，新增ProtoBuf格式数据生成，优化文章创作特性，支持将数据直接插入MySQL表。</p> 
<h3>2.1版更新内容</h3> 
<ul> 
 <li>支持ProtoBuf格式数据生成；</li> 
 <li>可将生成的数据直接插入MySQL表；</li> 
 <li>反向解析文章为YAML配置；</li> 
 <li>文章语义槽支持顺序、随机和固定引用；</li> 
 <li>输出生成的文章为多个文件；</li> 
 <li>修复了几个小的问题。</li> 
</ul> 
<h3>ZenData用途</h3> 
<div> 
 <p>ZenData主要两大功能：数据生成和数据解析。通过一个配置文件，可以使用ZenData生成您想要的各种数据。同样也可以对某一个数据文件，指定其数据类型定义的配置文件，完成到结构化数据的解析。</p> 
 <p>ZenData可以用于手工测试场景下面测试数据的准备，也可以用于自动化测试脚本里面的数据生成和解析。还可以一键生成海量数据用于性能和压力测试。</p> 
</div> 
<h3>ZenData特性</h3> 
<ol> 
 <li>简单无依赖，只有一个可执行文件，即可满足命令行生成和HTTP接口两种数据生成服务。</li> 
 <li>使用配置文件来生成数据，使用人员不需要有开发知识，即可上手应用。</li> 
 <li>提供了功能强大的语法，分组、区间、步长、循环、随机、格式化、函数和前后缀等，配置灵活性极强。</li> 
 <li>支持从文本文件中读取数据，方便用户对字段取值进行精确控制。</li> 
 <li>提供了Excel表格数据的标准SQL查询接口，使用更加灵活。</li> 
 <li>使用预制的序列（ranges）、实例（instances）、配置（config）对定义进行复用，以解决复杂数据格式的定义。</li> 
 <li>语法支持继承和扩展，为定义文件间的复用提供方便。</li> 
 <li>支持文本、JSON、XML、 CSV、SQL 、Excel、ProtoBuf多种输出格式。</li> 
 <li>可反向解析文章生成YAML配置模板；內置互联网黑话中文词库，文章创作方便而又有趣。</li> 
 <li>可以反向解析数据，可以对程序的输出进行解析，方便自动化测试脚本进行比对。</li> 
 <li>发行包內置了基础业务数据的定义文件（不断完善中）。</li> 
 <li>提供了HTTP接口数据生成服务，各种语言都可以方便调用。</li> 
 <li>內置Web版设计工具，减缓数据定义语法的学习曲线，数据管理和创作更高效。</li> 
</ol> 
<h3>2.1版下载地址</h3> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.1%2Fwin64%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-win64.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.1%2Fwin32%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-win32.zip</span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.1%2Flinux%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-linux.zip</span></a></li> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.1%2Fmac%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-mac.zip</span></a></p> </li> 
</ul> 
<p><span style="background-color:#ffffff; color:#232323">开源项目 </span><span style="background-color:#ffffff; color:#232323"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzendata" target="_blank"><span style="color:#337fe5">https://github.com/easysoft/zendata</span></a></p> 
<p>帮助文档  <span style="color:#337fe5"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zendata.cn%2Fbook%2Fzendata%2Fwhy-zendata-115.html" target="_blank"><span style="color:#337fe5">https://www.zendata.cn/book/zendata/why-zendata-115.html</span></a></span></p> 
<h3><span style="color:inherit">一键生成ProtoBuf格式数据</span></h3> 
<pre>zd.exe -c runtime\protobuf\person.proto -cls Person</pre> 
<p>生成的二进制文件在<span style="background-color:#f5f5f5; color:#666666">runtime\protobuf\</span><span style="color:inherit">data.bin中。</span></p> 
<h3><span style="color:inherit">"黑话连篇"的文章创作</span></h3> 
<p><span style="color:inherit">点击预览查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zendata.cn%2Fslang.php" target="_blank"><span style="color:#337fe5">https://www.zendata.cn/slang.php</span></a></span></p> 
<p><strong>数据定义文件</strong></p> 
<pre>author: ZenData
from: words.v1
title: 互联网黑话
type: article
version: 1.1

content: |
  # t=兄弟姐妹们
  # n=黑话名词
  # v=黑话动词

  <div><strong>互联网黑话</strong></div>
  <div>
    [t]，&#123;n&#125;是&#123;v&#125;&#123;n&#125;，&#123;v&#125;行业&#123;n&#125;。&#123;n&#125;是&#123;v&#125;&#123;n&#125;&#123;n&#125;，通过&#123;n&#125;和&#123;n&#125;达到&#123;n&#125;。
    &#123;n&#125;是在&#123;n&#125;采用&#123;n&#125;打法达成&#123;n&#125;。&#123;n&#125;&#123;n&#125;作为&#123;n&#125;为产品赋能，&#123;n&#125;作为&#123;n&#125;的评判标准。
    亮点是&#123;黑话名词&#125;，优势是&#123;n&#125;。&#123;v&#125;整个&#123;n&#125;，&#123;v&#125;&#123;n&#125;&#123;v&#125;&#123;n&#125;。&#123;n&#125;是&#123;n&#125;达到&#123;n&#125;标准。
  </div></pre> 
<p><span style="color:inherit"><strong>数据生成命令./zd -c yaml/article/chinese/slang/01.yaml </strong></span></p> 
<p><span style="color:inherit"><img alt src="https://www.zendata.cn/file.php?f=202104/f_abeb734e4373e96b58ec924c7bcba7d7&t=png&o=&s=&v=1615794273" referrerpolicy="no-referrer"></span></p> 
<h3>生成Apache访问日志</h3> 
<div> 
 <p><strong>使用yaml/log/apache.access.v1.yaml文件生成100万条Apache访问日志</strong></p> 
 <p><img alt src="https://www.zendata.cn/file.php?f=202104/f_94b938a56fb753899b06f61303ea94e0&t=png&o=&s=&v=1615794273" referrerpolicy="no-referrer"></p> 
</div> 
<h3><strong>数据设计工具界面</strong></h3> 
<p><strong>我的数据</strong></p> 
<p><img alt src="https://www.zendata.cn/file.php?f=202102/f_fce86378e60ea23a7588b9ecf7c09359&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></p> 
<p><strong>內置数据</strong></p> 
<p><img alt src="https://www.zendata.cn/file.php?f=202102/f_a5b68dcb1f1fa906282373a6c48bcfbf&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></p> 
<p><strong>数据设计器</strong></p> 
<p><img alt src="https://www.zendata.cn/file.php?f=202102/f_225c493f398c7f55825d851d05d9288d&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            