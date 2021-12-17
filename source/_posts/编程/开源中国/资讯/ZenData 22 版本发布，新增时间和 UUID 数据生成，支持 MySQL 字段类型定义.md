
---
title: 'ZenData 2.2 版本发布，新增时间和 UUID 数据生成，支持 MySQL 字段类型定义'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://www.zendata.cn/file.php?f=202112/f_4b4de17a81c5e2ff378b0c1ca1b56ee8&t=png&o=&s=&v=1632638904'
author: 开源中国
comments: false
date: Fri, 17 Dec 2021 15:54:00 GMT
thumbnail: 'https://www.zendata.cn/file.php?f=202112/f_4b4de17a81c5e2ff378b0c1ca1b56ee8&t=png&o=&s=&v=1632638904'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div style="margin-left:0; margin-right:0; text-align:start">
  <span><span style="color:#333333">ZenData2.2版本发布，</span><span style="color:#333333">优化了多处数据定义语法,</span><span style="color:#333333">新增Uuid格式数据生成，增加对Mysql数据库字段定义的支持.</span></span>
 </div> 
 <h3 style="text-align:start"><span><strong style="color:#333333">2.2版更新内容</strong></span></h3> 
 <ul> 
  <li> <p><span><span style="color:#333333">从SQL生成数据定义时，增加了对MySQL字段类型的支持,如longtext、int等；</span></span></p> </li> 
  <li> <p><span><span style="color:#333333">新增时间表达式，如year(Y),month(M),day(D),week(w),hour(h),minute(m)；</span></span></p> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">优化UUID数据生成，<span>使用fomat:"uuid(-)"</span><span>函数表达式</span>；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">服务请求模式下，去掉生成临时数据文件的步骤，提高并发性能；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">修复Use属性下，无法解析多个Instances的问题；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span>修复loop区间生成的数据的问题；</span></span>
   </div> </li> 
  <li> <p><span><span>其他一些问题的修复。</span></span></p> </li> 
 </ul> 
 <h3 style="text-align:start"><span><strong style="color:#333333">ZenData用途</strong></span></h3> 
 <div style="text-align:start"> 
  <div style="margin-left:0; margin-right:0">
   <span><span style="color:#333333">ZenData主要两大功能：数据生成和数据解析。通过一个配置文件，可以使用ZenData生成您想要的各种数据。同样也可以对某一个数据文件，指定其数据类型定义的配置文件，完成到结构化数据的解析。</span></span>
  </div> 
  <div style="margin-left:0; margin-right:0">
    
  </div> 
  <div style="margin-left:0; margin-right:0">
   <span><span style="color:#333333">ZenData可以用于手工测试场景下面测试数据的准备，也可以用于自动化测试脚本里面的数据生成和解析，还可一键生成海量数据用于性能和压力测试。</span></span>
  </div> 
 </div> 
 <h3 style="text-align:start"><span><strong style="color:#333333">ZenData特性</strong></span></h3> 
 <ol> 
  <li> 
   <div>
    <span><span style="color:#333333">简单无依赖，只有一个可执行文件，即可满足命令行生成和HTTP接口两种数据生成服务；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">使用配置文件来生成数据，使用人员不需要有开发知识，即可快速上手应用；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">提供了简明、强大的数据定义语法，如分组、区间、步长、循环、随机、格式化、前后缀、函数和表达式等，配置灵活、扩展方便；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">支持从文本文件中读取数据，方便用户对字段取值进行精确控制；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">提供了Excel表格数据的标准SQL查询接口，数据维护和萃取更加灵活；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">使用预制的序列（ranges）、实例（instances）、配置（config）对定义进行复用，以解决复杂数据的定义；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">语法支持继承和扩展，为数据定义文件间的复用提供方便；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">支持文本、JSON、XML、 CSV、SQL 、Excel、ProtoBuf多种输出格式；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">可反向解析文章生成YAML配置模板；內置互联网黑话中文词库，文章创作方便而又有趣；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">可反向解析二维表格形式的数据，生成结构化数据，方便用于自动化测试脚本中的验证点比对；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">发行包內置了常见的基础业务数据的定义文件；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">提供了HTTP接口形式的数据生成服务API，各种语言都可以方便调用；</span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span style="color:#333333">內置Web版设计工具，减缓数据定义语法的学习曲线，数据管理和创作更高效。</span></span>
   </div> </li> 
 </ol> 
 <h3 style="text-align:start"><span><strong style="color:#333333">2.2版下载地址</strong></span></h3> 
 <ul> 
  <li> 
   <div>
    <span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.2%2Fwin64%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-win64.zip</span></a></span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.2%2Fwin32%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-win32.zip</span></a></span></span>
   </div> </li> 
  <li> 
   <div>
    <span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.2%2Flinux%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-linux.zip</span></a></span></span>
   </div> </li> 
  <li> 
   <div style="margin-left:0; margin-right:0">
    <span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdl.cnezsoft.com%2Fzd%2F2.2%2Fmac%2Fzd.zip" target="_blank"><span style="color:#337fe5">zd-mac.zip</span></a></span></span>
   </div> </li> 
 </ul> 
 <div>
  <span><span style="color:#232323">开源项目 </span><span style="color:#232323"> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Feasysoft%2Fzendata" target="_blank">https://github.com/easysoft/zendata</a></span>
 </div> 
 <div style="margin-left:0; margin-right:0; text-align:start">
  <span><span style="color:#232323">帮助文档  </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.zendata.cn%2Fbook%2Fzendata%2Fwhy-zendata-115.html" target="_blank">https://www.zendata.cn/book/zendata/why-zendata-115.html</a></span>
 </div> 
 <h3><span><span style="color:inherit">生成时间格式数据</span></span></h3> 
 <div style="text-align:start"> 
  <p style="margin-left:0; margin-right:0"><span><strong style="color:#333333"><strong>数据定义</strong></strong></span></p> 
  <pre><span>fields:
  - field: date
    from: time.date.v1.yaml
    use: date
    postfix: " "


  - field: cn_date
    from: time.date.v1.yaml
    use: chinese
    postfix: " "


  - field: time
    from: time.time.v1.yaml
    use: time
    postfix: " "


  - field: time1     # 生成时间数据，以当前时间为准，从一月前到一周后。
    range: "(-1M)-(+1w):60"        # 支持当前时间的运算，Y、M、D、W、h、m、s分别对应年、月、日、周、时、分、秒。
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time2         # 生成时间数据，指定起止时间的方式，从早上9点到今天结束，间隔1分钟（60秒）。
    range: "20210101 000000-20210101 230000:60"    # 起始、结束时间用-分隔，默认为当天的开始和结束时间。
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time3   # 只设置一个时间时，默认当作起始时间，结束时间为当前日期的23时59分59秒
    range: "20210821 000000:60"  # 和20210821 000000-:60效果是一样的
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time4
    range: "-20210830 235959:60" # 省略起始时间的用法
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time5     # 生成时间数据，以当前时间为准，从一月前到一周后。
    range: "(-1M)-(+1w):60m"        # 步长支持Y、M、D、W、h、m、s分别对应年、月、日、周、时、分、秒
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time6     # 生成时间数据，以当前时间为准，从一月前到一周后。
    range: "(-1M)-(+1w):1D"        # 步长支持Y、M、D、W、h、m、s分别对应年、月、日、周、时、分、秒
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time7     # 生成时间数据，以当前时间为准，从一月前到一周后。
    range: "(+1w)-(-1M):-1D"        # 步长为-1天
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"
    postfix: "\t"


  - field: time8     # 生成时间数据，以当前时间为准，从一月前到一周后。
    range: "(+1w)-(-1M):1D"        # 设置步长为1天，但是会自动的根据起止时间调整正负，实际为-1天
    type: timestamp
    format: "YY/MM/DD hh🇲🇲ss"</span></pre> 
  <p><span><span><strong>执行命令</strong></span></span></p> 
  <p> </p> 
  <pre><span>zd -d demo/28_datetime.yaml</span></pre> 
  <p> </p> 
  <p><span><strong>执行结果</strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span><img alt src="https://www.zendata.cn/file.php?f=202112/f_4b4de17a81c5e2ff378b0c1ca1b56ee8&t=png&o=&s=&v=1632638904" referrerpolicy="no-referrer"></span></p> 
  <p style="margin-left:0; margin-right:0"> </p> 
  <h3><span><span>生成UUID格式数据</span></span></h3> 
  <p><span><strong><strong>数据定义</strong></strong></span></p> 
  <pre><span>fields:
  - field: field_uuid
    format: "uuid(-)"</span></pre> 
  <p><span><strong>执行命令</strong></span></p> 
  <pre><span><strong>zd -d demo/29_uuid.yaml</strong></span></pre> 
  <p><span><strong>执行结果</strong></span></p> 
  <div style="margin-left:0; margin-right:0">
   <span><img alt src="https://www.zendata.cn/file.php?f=202112/f_fc406ed9218155ad2203a7167a4f6de2&t=png&o=&s=&v=1632638904" referrerpolicy="no-referrer"></span>
  </div> 
  <div>
    
  </div> 
  <p> </p> 
  <p style="margin-left:0; margin-right:0"><span><strong>新增MySQL字段属性的支持</strong></span></p> 
  <p style="margin-left:0; margin-right:0"><span><strong>执行命令</strong></span></p> 
  <pre><span>zd -i demo/field_test.sql -o demo/output</span></pre> 
  <p style="margin-left:0; margin-right:0"><span><span><strong>生成结果</strong></span></span></p> 
  <pre><span><strong>title: table field_test
desc: ""
author: automated export
version: "1.0"
fields:
    - field: Bit
      range: 0,1
    - field: TinyInt
      range: 0-255
    - field: SmallInt
      range: 0-65535
    - field: MediumInt
      note: "MEDIUMINT [0,2^24-1]"
      range: 0-65535
    - field: GeometryCollection
      range: "GEOMETRYCOLLECTION"
    - field: Int
      note: "INI [0,2^32-1]"
      range: 0-100000
    - field: BigInt
      note: "BIGINT [0,2^64-1]"
      range: 0-100000</strong></span></pre> 
  <div style="margin-left:0; margin-right:0"> 
   <h3><span><strong>数据设计工具</strong></span></h3> 
   <p><span><strong>我的数据</strong></span></p> 
   <p><span><img alt src="https://www.zendata.cn/file.php?f=202102/f_fce86378e60ea23a7588b9ecf7c09359&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></span></p> 
   <p><span><strong>內置数据</strong></span></p> 
   <p><span><img alt src="https://www.zendata.cn/file.php?f=202102/f_a5b68dcb1f1fa906282373a6c48bcfbf&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></span></p> 
   <p><span><strong>数据设计器</strong></span></p> 
   <p><span><img alt src="https://www.zendata.cn/file.php?f=202102/f_225c493f398c7f55825d851d05d9288d&t=png&o=&s=&v=1608859104" referrerpolicy="no-referrer"></span></p> 
  </div> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            