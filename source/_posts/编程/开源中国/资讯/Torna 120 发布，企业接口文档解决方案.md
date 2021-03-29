
---
title: 'Torna 1.2.0 发布，企业接口文档解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d412329a276f4655bc4f54c3cefa00871aa.png'
author: 开源中国
comments: false
date: Mon, 29 Mar 2021 11:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d412329a276f4655bc4f54c3cefa00871aa.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Torna 1.2.0 发布，本次更新内容如下：</span></p> 
<ul> 
 <li>[feat]新增全局请求参数</li> 
 <li>[feat]新增全局返回参数</li> 
 <li>[refactor]优化字典管理交互</li> 
 <li>[refactor]优化模块设置交互</li> 
 <li>[refactor]优化加载文档性能问题</li> 
</ul> 
<p>本次更新重点是新增全局请求参数和全局返回参数</p> 
<h2><span style="background-color:#fbfbfb; color:#24292e">全局请求参数</span></h2> 
<p><span style="background-color:#fbfbfb; color:#24292e">设置了全局请求参数，每个接口请求都要带上这个参数，设置方式：前往</span><code>模块配置</code><span style="background-color:#fbfbfb; color:#24292e"> -> </span><code>全局请求参数</code><span style="background-color:#fbfbfb; color:#24292e">进行配置</span></p> 
<p><span style="background-color:#fbfbfb; color:#24292e">设置完毕后访问文档浏览页，请求参数列表中都会出现配置的全局请求参数。</span></p> 
<h2 style="text-align:left">全局返回参数</h2> 
<p style="text-align:left">全局返回参数配置方式同全局请求参数一样，只不过这里多了数据节点。</p> 
<ul> 
 <li>为何要数据节点？</li> 
</ul> 
<p style="text-align:left">假如您的项目使用AOP技术做到统一结果返回，如：</p> 
<pre><code class="language-json">&#123;
    "code": "1000",
    "msg": "success",
    "data": &#123;...&#125;
&#125;</code></pre> 
<p style="text-align:left">其中，code, msg, data部分属于全局返回参数，<code>&#123;...&#125;</code>属于业务参数。</p> 
<p style="text-align:left">假设controller只返回业务结果</p> 
<pre>@<span style="color:#cc7832">RequestMapping</span>(<span style="color:#6a8759">"/findAll"</span>)
<span style="color:#cc7832">public </span>List<span style="color:#cc7832"><</span>User<span style="color:#cc7832">> </span>findAll()&#123;
    <span style="color:#cc7832">return </span>userService.list();
&#125;</pre> 
<div>
 这样只能定义业务返回参数，外层的全局参数很难定义（当然也有解决办法）。
</div> 
<p style="text-align:left">在这种情况下，可以配置全局返回参数，然后指定数据节点，具体操作方式如下：</p> 
<p style="text-align:left">前往<code>模块配置</code> -> <code>全局返回参数</code>，点击<code>添加</code></p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-d412329a276f4655bc4f54c3cefa00871aa.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">填写表单</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-c64743284b4ec73a43ec85db1b3668773cc.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">这里顺便指定了关联枚举，用来解释各个code值，可以事先前往<code>字典管理</code>进行配置</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-20d19679ef57c8f31975b3ce38652654427.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">接着使用同样的方式添加<code>msg</code>字段。</p> 
<p style="text-align:left">最后添加<code>data</code>字段，因为data字段是数据节点，需要设置为数据节点。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-77f4591edb409f1ff6a284a8e2af5b31157.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left">前往文档浏览页，展示结果如下：</p> 
<p><img src="https://oscimg.oschina.net/oscnet/up-8ae093cec465dc045de5f32479a81e0931c.png" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p style="text-align:left">关于<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Ftorna.cn" target="_blank">Torna</a></p> 
<p style="text-align:left">企业接口文档解决方案，目标是让文档管理变得更加方便、快捷。Torna采用团队协作的方式管理和维护项目API文档，将不同形式的文档纳入进来，形成一个统一的维护方式。</p> 
<p style="text-align:left"><img src="https://gitee.com/durcframework/torna/raw/master/front/public/static/images/arc.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            