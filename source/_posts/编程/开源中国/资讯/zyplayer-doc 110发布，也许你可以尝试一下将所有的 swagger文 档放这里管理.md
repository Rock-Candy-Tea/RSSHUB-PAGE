
---
title: 'zyplayer-doc 1.1.0发布，也许你可以尝试一下将所有的 swagger文 档放这里管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0331e0f8db55c17a24434595667802da495.png'
author: 开源中国
comments: false
date: Sun, 19 Dec 2021 21:30:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0331e0f8db55c17a24434595667802da495.png'
---

<div>   
<div class="content">
                                                                                            <h1>项目介绍</h1> 
<p>zyplayer-doc是一款前后端完全开源的在线文档工具，现有API接口文档（Swagger、OpenApi、自建接口）、WIKI文档、数据库文档（数据库表结构查看管理、SQL执行）、Dubbo文档。</p> 
<p>在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.zyplayer.com%2Fzyplayer-doc-manage%2Fdoc-wiki%23%2Fpage%2Fshare%2Fview%3FpageId%3D360%26space%3D23f3f59a60824d21af9f7c3bbc9bc3cb" target="_blank">zyplayer-doc使用文档</a></p> 
<p>体验地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdoc.zyplayer.com" target="_blank">http://doc.zyplayer.com</a> 账号：zyplayer 密码：123456</p> 
<p>开源地址：<a href="https://gitee.com/zyplayer/zyplayer-doc">https://gitee.com/zyplayer/zyplayer-doc</a></p> 
<p>BUG反馈：<a href="https://gitee.com/zyplayer/zyplayer-doc/issues">https://gitee.com/zyplayer/zyplayer-doc/issues</a></p> 
<h1>本次升级内容</h1> 
<blockquote> 
 <p>本次升级针对数据库模块做了许多易用性的更新，将Swagger文档模块重构为了API接口文档管理模块，提供更完善的Swagger文档、OpenApi文档的展示和调试体验。</p> 
</blockquote> 
<p>注意：本次升级有新的脚本，需先执行增量更新SQL再升级</p> 
<h2>全局</h2> 
<ol> 
 <li>用户权限控制重构</li> 
 <li>去掉对es、grpc的支持和依赖，专注核心模块的开发</li> 
 <li>默认去掉对hive的包依赖，编译结果文件瘦身100M+</li> 
 <li>maven依赖关系优化，依赖的maven包升级，解决依赖混乱问题</li> 
 <li>增加build.bat的支持，支持jar直接启动，去掉历史遗留的无用前端代码</li> 
</ol> 
<h2>数据库模块</h2> 
<ol> 
 <li>优化数据查询的展示效果</li> 
 <li>SQL编辑器自动提示优化，更加智能，可拖动改变左侧菜单宽度</li> 
 <li>多Tab标签页切换问题修改</li> 
 <li>表数据查看页增加选择展示列功能</li> 
</ol> 
<h2>API接口文档模块</h2> 
<ol> 
 <li>使用vite+vue3+antdv重构swagger文档展示</li> 
</ol> 
<h2>WIKI文档模块</h2> 
<ol> 
 <li>#I3BMNS 代码块高亮，增加判空和状态判断</li> 
 <li>增加导航和拖动改变左侧菜单宽度功能，编辑器默认改为markdown模式</li> 
 <li>修复wiki有序列表不展示序号问题</li> 
</ol> 
<h1>API接口文档模块重构说明</h1> 
<h2>和同类型产品相比有何优势？</h2> 
<p>同类型的产品有：eolink、apizza、Apifox、ApiPost、EasyAPI、docway等等，提供有云端接口文档管理服务、私有化部署（收费），产品级的东西使用起来确实舒服， 开源产品有：torna、knife4j、https://gitee.com/shuzhikai/moyu、YApi等，个个开源大佬都是人才，功能强大，代码又写的漂亮，用户量又高，但我觉得zyplayer-doc还是有自己的特别之处，这里就不进行对比了，专业人士也可以去写点对比文章，促进大家成长，坚持开源都挺了不起的，还是希望你们自己去体验对比，找到适合自己的工具。</p> 
<h2>重构缘由</h2> 
<p>本来这个版本准备把数据库模块做的更完善的，flag都立好了，但发现总有用户问起swagger文档展示相关问题，又不想在老版本修改了，正好Vue3发布了，antdv等前端框架也跟上了，新技术总是如此的吸引人，于是用最前沿的技术去重构了一版API接口文档，完全重构的，性能更好，代码更清晰易维护，但对swagger的解析还没做到百分百的兼容，详细研究了一下swagger的标准，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fswagger.io%2Fspecification%2Fv2" target="_blank">https://swagger.io/specification/v2</a> ，里面的属性超级多， 如果想按照标准完全解析，我觉得很多属性根本用不上，而且测试也复杂，很容易覆盖不到。 最后权衡下来本项目的原则是有用到哪些就解析哪些属性，没必要来全套，大家一起来维护完善，共建共享。同时看了下新版本的标准叫做OpenApi，结构定义改动很大，我看smart-doc也支持导出为此标准的接口文档导出，于是对此标准也做了支持，现在，你使用==smart-doc==工具生成的文档也可以直接放入本项目中展示了！本项目对swagger或OpenApi标准文档解析的原则是前端解析，能快速适配没支持到的属性，可操作性高一点。</p> 
<h2>现在使用稳定可靠吗？</h2> 
<p>本工具的升级都是向后兼容的，每次升级都有提供具体的升级SQL，不会有大的破坏性更新，所以放心使用，有你的支持才有提升，种子用户支持手把手支持哦。还有好多厉害的功能想要这个版本支持到的，但还是得有一个版本规划，在合适的时候就提供一个稳定版本还是很有必要的，慢慢的成长，如果你有使用，还是希望你能多提意见共同改进。</p> 
<h2>只是看swagger文档启动本项目成本太高？</h2> 
<p>如果你觉得用此项目展示swagger文档太重，你也可以尝试使用<a href="https://gitee.com/zyplayer/swagger-mg-ui">swagger-mg-ui</a>，纯前端项目，零侵入性、零后端代码，只是一个解析swagger标准文档的前端项目，引入后无任何负担，值得用于尝试替换swagger-ui。前端代码和本项目是一套，新设计，新技术，新体验，独立的后端项目看文档我也更倾向于这种方式来接入使用，简单，引入后即使不用也无任何影响，唯一的缺点就是还太年轻，需要大家的不断锤炼。</p> 
<pre><code class="language-xml"><!-- https://mvnrepository.com/artifact/com.zyplayer/swagger-mg-ui -->
<dependency>
    <groupId>com.zyplayer</groupId>
    <artifactId>swagger-mg-ui</artifactId>
    <version>2.0.1</version>
</dependency>
</code></pre> 
<h1>WIKI文档页</h1> 
<p><img height="956" src="https://oscimg.oschina.net/oscnet/up-0331e0f8db55c17a24434595667802da495.png" width="1919" referrerpolicy="no-referrer"></p> 
<h1>数据库模块</h1> 
<p><img alt height="960" src="https://oscimg.oschina.net/oscnet/up-6caa2a287a3d115d7bfa2f26ce771bfd74c.png" width="1917" referrerpolicy="no-referrer"></p> 
<h1>API接口文档管理模块</h1> 
<p><img height="586" src="https://oscimg.oschina.net/oscnet/up-353179247053d85002459785137cf7f4a90.png" width="1920" referrerpolicy="no-referrer"></p> 
<p><img height="834" src="https://oscimg.oschina.net/oscnet/up-cc510729b03cd59e15c6d23494c45233afc.png" width="1920" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            