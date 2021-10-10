
---
title: 'Hutool 5.7.14 发布，主题 T 恤来袭'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
author: 开源中国
comments: false
date: Sat, 09 Oct 2021 23:58:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img src="https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hutool是一个小而全的Java工具类库，通过静态方法封装，降低相关API的学习成本，提高工作效率，使Java拥有函数式语言般的优雅，让Java语言也可以“甜甜的”。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hutool中的工具方法来自于每个用户的精雕细琢，它涵盖了Java开发底层代码中的方方面面，它既是大型项目开发中解决小问题的利器，也是小型项目中的效率担当；</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Hutool是项目中“util”包友好的替代，它节省了我们对项目中公用类和公用工具方法的封装时间，使开发专注于业务，同时可以最大限度的避免封装不完善带来的bug。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">-------------------------------------------------------------------------------------------------------------------</p> 
<p>经过几个月的精心准备，Hutool终于有了相关的周边商品——主题T恤，它是这个样子：</p> 
<p><img height="300" src="https://gd4.alicdn.com/imgextra/i2/1072910175/O1CN01z8M5FF1DAC1NrCGSI_!!1072910175.jpg" width="300" referrerpolicy="no-referrer"></p> 
<p>颜色是接近黑色的藏蓝色，LOGO+撞色是开发者和合作方设计的结果。只是……上架后开始入秋了，哎……</p> 
<p>为了规避广告嫌疑，我就不贴购买链接了，请大家访问Hutool的主页：https://hutool.cn/ 或项目的README中找到对应的链接购买。</p> 
<p>我们为什么要做周边呢？我们希望Hutool一直保持开源开放的走下去，并始终保持活跃，捐赠、主页文档广告和周边产品都是不错的经济支持，同时也不会让代码本身沾满商业气息。另一方面，Hutool的周边可以让这个局限于Java的开源工具更广的传播开来，从而使Hutool不只是一段开源代码，而是一种开源精神和象征。</p> 
<p><span style="background-color:#ffffff; color:#333333">-------------------------------------------------------------------------------------------------------------------</span></p> 
<h1 style="margin-left:0; margin-right:0; text-align:left">5.7.14 (2021-10-09)</h1> 
<h3 style="margin-left:0; margin-right:0; text-align:left">🐣新特性</h3> 
<ul> 
 <li>【extra 】 修复HttpCookie设置cookies的方法，不符合RFC6265规范问题（issue#I4B70D@Gitee）</li> 
 <li>【http 】 优化Browser版本正则判断</li> 
 <li>【setting】 增加YamlUtil</li> 
 <li>【extra 】 SenvenZExtractor改名为SevenZExtractor，增加getFirst、get方法</li> 
 <li>【core 】 DateConverter修改返回java.util.Date而非DateTime（issue#I4BOAP@Gitee）</li> 
 <li>【core 】 增加IterableIter、ComputeIter</li> 
 <li>【core 】 CsvConfig增加disableComment方法（issue#1842@Github）</li> 
 <li>【core 】 DateTime构造和DateUtil.parse可选是否宽松模式（issue#1849@Github）</li> 
 <li>【core 】 TreeBuilder增加部分根节点set方法（issue#1848@Github）</li> 
 <li>【core 】 优化Base64.isBase64方法：减少一次多余的判断（pr#1860@Github）</li> 
 <li>【cache 】 优化FIFOCache未设置过期策略时，无需遍历判断过期对象（pr#425@Gitee）</li> 
 <li>【core 】 增加Opt类（pr#426@Gitee）</li> 
 <li>【core 】 Week增加of重载，支持DayOfWek（pr#1872@Github）</li> 
 <li>【poi 】 优化read，避免多次创建CopyOptions（issue#1875@Github）</li> 
 <li>【core 】 优化CsvReader，实现可控遍历（pr#1873@Github）</li> 
 <li>【core 】 优化Base64.isBase64判断（pr#1879@Github）</li> 
 <li>【core 】 新增StrFormatter.formatWith（pr#430@Gitee）</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">🐞Bug修复</h3> 
<ul> 
 <li>【http 】 修复HttpCookie设置cookies的方法，不符合RFC6265规范问题（pr#418@Gitee）</li> 
 <li>【http 】 修复Extractor中filter无效问题</li> 
 <li>【json 】 修复JSONGetter.getJSONArray判断null的问题（issue#I4C15H@Gitee）</li> 
 <li>【db 】 修复Condition没占位符的情况下sql没引号问题（issue#1846@Github）</li> 
 <li>【cache 】 修复FIFOCache中remove回调无效问题（pr#1856@Github）</li> 
 <li>【json 】 修复JSONArray.set中，index为0报错问题（issue#1858@Github）</li> 
 <li>【core 】 修复FileUtil.checkSlip中getCanonicalPath异常引起的问题（issue#1858@Github）</li> 
</ul>
                                        </div>
                                      
</div>
            