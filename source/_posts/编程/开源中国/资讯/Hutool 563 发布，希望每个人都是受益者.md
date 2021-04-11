
---
title: 'Hutool 5.6.3 发布，希望每个人都是受益者'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
author: 开源中国
comments: false
date: Sun, 11 Apr 2021 10:56:00 GMT
thumbnail: 'https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg'
---

<div>   
<div class="content">
                                                                                            <p><img src="https://static.oschina.net/uploads/img/201803/21114512_tLDC.jpg" referrerpolicy="no-referrer"></p> 
<p><span style="background-color:#ffffff; color:#333333">Hutool是一个小而全的Java工具类库，通过静态方法封装，降低相关API的学习成本，提高工作效率，使Java拥有函数式语言般的优雅，让Java语言也可以“甜甜的”。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">-------------------------------------------------------------------------------------------------------------------</span></p> 
<p>Hutool作为一个工具类库，它的存在更像是一种开源精神的传播者，也是“代码洁癖”精神的倡导者。我们为了从堆积如山的混乱代码中挣脱出来，有的人制定了繁琐的`code style`，有的人不断分享最佳实践，而Hutool则是把代码变成规范。</p> 
<p><span style="background-color:#ffffff; color:#000000">Hutool一直是一个开放、包容的开源项目，项目中的工具方法来源也非常广泛（博客、其他开源项目、StackOverflow），因此允许并鼓励任何人无条件可以：</span></p> 
<p><br> <span style="background-color:#ffffff; color:#000000">1.  将Hutool用于商业、培训等任何合法场景；</span><br> <span style="background-color:#ffffff; color:#000000">2.  复制、修改Hutool中的任意代码且无需声明；</span><br> <span style="background-color:#ffffff; color:#000000">3.  复制修改和传播Hutool官方文档；</span><br> <span style="background-color:#ffffff; color:#000000">4.  鼓励自行创作Hutool相关的书籍、博客、文档、视频教程等内容（收费也可）；</span><br> <span style="background-color:#ffffff; color:#000000">5.  鼓励播主、培训机构培训Hutool工具的任何内容（收费也可）；</span><br>  </p> 
<p>Hutool的自信源自对自身活力的自信，因为任何复制后的代码都失去了这份活力，而鼓励大家创作则是希望Hutool像蒲公英一样传播开来，而每一位传播者也希望因Hutool受益。</p> 
<p><span style="background-color:#ffffff; color:#000000">Hutool希望成为一个伟大的开源项目，也希望得到大家的认可和赞美，仅此而已。</span></p> 
<p><span style="background-color:#ffffff; color:#333333">-------------------------------------------------------------------------------------------------------------------</span></p> 
<p><span style="background-color:#ffffff; color:#333333">其他更新如下：</span></p> 
<pre><em>### </em><em>新特性
</em><span style="color:#cc7832">* </span>【core   】     修改数字转换的实现，增加按照指定端序转换（pr#1492@Github）
<span style="color:#cc7832">* </span>【core   】     修改拆分byte数组时最后一组长度的规则（pr#1494@Github）
<span style="color:#cc7832">* </span>【core   】     新增根据日期获取节气（pr#1496@Github）
<span style="color:#cc7832">* </span>【core   】     mapToBean()添加对布尔值is前缀的识别（pr#294@Gitee）
<span style="color:#cc7832">* </span>【core   】     农历十月十一月改为寒月和冬月（pr#301@Gitee）
<span style="color:#cc7832">* </span>【core   】     增加港澳台电话正则（pr#301@Gitee）
<span style="color:#cc7832">* </span>【core   】     增加银行卡号脱敏（pr#301@Gitee）
<span style="color:#cc7832">* </span>【cache  】     使用LongAddr代替AtomicLong（pr#301@Gitee）
<span style="color:#cc7832">* </span>【cache  】     EnumUtil使用LinkedHashMap（pr#304@Gitee）
<span style="color:#cc7832">* </span>【crypto 】     SymmetricCrypto支持大量数据加密解密（pr#1497@Gitee）
<span style="color:#cc7832">* </span>【http   】     SoapClient增加针对不同协议的头信息（pr#305@Gitee）
<span style="color:#cc7832">* </span>【http   】     HttpRequest支持307、308状态码识别（issue#1504@Github）
<span style="color:#cc7832">* </span>【core   】     CharUtil.isBlankChar增加\u0000判断（pr#1505@Github）
<span style="color:#cc7832">* </span>【extra  】     添加Houbb Pinyin支持（pr#1506@Github）
<span style="color:#cc7832">* </span>【core   】     添加LambdaUtil（pr#295@Gitee）
<span style="color:#cc7832">* </span>【core   】     添加StrPool和CharPool
<span style="color:#cc7832">* </span>【extra  】     CglibUtil增加toBean和fillBean方法
<span style="color:#cc7832">* </span>【db     】     增加DriverNamePool

<em>### Bug</em><em>修复
</em><span style="color:#cc7832">* </span>【core   】     修复Validator.isUrl()传空返回true（issue#I3ETTY@Gitee）
<span style="color:#cc7832">* </span>【db     】     修复数据库driver根据url的判断识别错误问题（issue#I3EWBI@Gitee）
<span style="color:#cc7832">* </span>【json   】     修复JSONStrFormatter换行多余空行问题（issue#I3FA8B@Gitee）
<span style="color:#cc7832">* </span>【core   】     修复UrlPath中的+被转义为空格%20的问题（issue#1501@Github）
<span style="color:#cc7832">* </span>【core   】     修复DateUtil.parse方法对UTC时间毫秒少于3位不识别问题（issue#1503@Github）</pre>
                                        </div>
                                      
</div>
            