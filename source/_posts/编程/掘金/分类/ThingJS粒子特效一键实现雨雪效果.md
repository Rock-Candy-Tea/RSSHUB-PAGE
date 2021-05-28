
---
title: 'ThingJS粒子特效一键实现雨雪效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/756f30b518ec485bba4acaf2ce2d797a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 22:18:55 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/756f30b518ec485bba4acaf2ce2d797a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>1、粒子效果</p>
<p>2、加载场景</p>
<p>3、不同粒子效果实现</p>
<p>在做3D项目时，我们经常需要模拟下雨，下雪的天气，有时也会模拟喷泉、着火等效果。这些效果需要使用名为粒子系统(particle)的技术来实现。使用<a href="https://www.thingjs.com/guide/main/" target="_blank" rel="nofollow noopener noreferrer">ThingJS</a>可以快速编写粒子效果，比如：下雨、下雪（可以控制雨雪大小）、喷水、火焰效果等，甚至可以通过对接第三方的数据，实时控制三维场景的效果（比如：对接天气接口）。</p>
<p><strong>1、粒子效果</strong></p>
<p>ThingJS 提供 ParticleSystem 物体类来实现粒子效果。自己制作粒子效果需要图片处理、写代码、3D渲染， 是个很艰巨的任务，需要掌握大量 3D 算法知识，还要掌握 shader 语言。ThingJS封装了粒子效果的实现方法，减少了代码量和开发投入，更受3D开发初学者的欢迎，直接用query查询API接口，在场景中加入火焰效果。</p>
<p>ThingJS内置一些粒子效果可以直接调用,可点击在线开发选择代码块进行调用。</p>
<p><strong>2、</strong> <strong>加载场景</strong></p>
<p>CampusBuilder（又称模模搭）搭建场景完成后，在ThingJS直接加载url进行二次开发。</p>
<pre><code class="copyable">// 加载场景代码 
var app = new THING.App(&#123;
 url: 'https://www.thingjs.com/static/models/storehouse' // 场景地址
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>3、不同粒子特效实现</strong></p>
<ul>
<li><strong>火焰效果</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/756f30b518ec485bba4acaf2ce2d797a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="copyable">/**
 * 通过创建粒子实现火焰效果
 */
function createFire() &#123;
 resetAll();
 // 创建粒子
 var particle = app.create(&#123;
 id: 'fire01',
 type: 'ParticleSystem',
 name: 'Fire',
 parent: app.query('car01')[0],
 url: 'https://model.3dmomoda.com/models/19061018snbajhvuzrheq9sbgwdoefuk/0/particles',
 localPosition: [0, 0, 0] // 设置粒子相对于父物体的位置
 &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>飘雪效果</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4c62bf1274342c6be20c6192fa8a755~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="copyable">/**
 * 通过创建粒子实现飘雪效果
 */
function createSnow() &#123;
 resetAll();
 // 创建降雪效果
 var particleSnow = app.create(&#123;
 type: 'ParticleSystem',
 id: 'No1234567',
 name: 'Snow',
 url: 'https://model.3dmomoda.com/models/18112014q3t8aunaabahzxbxcochavap/0/particles',
 position: [0, 50, 0]
 &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>喷水效果</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d34e1862338f4348b0bbbc17a8ea05ee~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="copyable">/**
 * 通过创建粒子实现喷水效果
 */
function createWater() &#123;
 resetAll();
 // 创建喷水效果
 var particle = app.create(&#123;
 id: 'water01',
 type: 'ParticleSystem',
 name: 'Water',
 url: 'https://model.3dmomoda.com/models/19081611ewlkh7xqy71uzixefob8uq1x/0/particles',
 position: [0, 0, 5]
 &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>降雨效果</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb6fa23e49804ae3b48dfef49a974515~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码如下：</p>
<pre><code class="copyable">/**
 * 通过创建粒子实现降雨效果
 */
function createByParticle() &#123;
 resetAll();
 // 创建粒子
 var particle = app.create(&#123;
 type: 'ParticleSystem',
 name: 'Rain',
 url: 'https://model.3dmomoda.com/models/18112113d4jcj4xcoyxecxehf3zodmvp/0/particles',
 position: [0, 300, 0],
 complete: function (ev) &#123;
 ev.object.scale = [10, 10, 10];
 &#125;
 &#125;);
 // 设置粒子最大密度
 particle.setGroupAttribute('maxParticleCount', 1000);
 // 设置粒子最小密度
 particle.setParticleAttribute('particleCount', 500);
 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>雨雪天气，是通过粒子图片渲染来实现的，我们可以通过控制粒子数量的最大密度和最小密度来实现降雨降雪量大小。</p>
<ul>
<li>
<p><strong>清除粒子效果</strong></p>
<p>function resetAll() &#123;
// 获取当前已创建的粒子
var particle = app.query('.ParticleSystem');
// 判断当前有无创建的粒子
if (particle) &#123;
// 存在，将已创建的粒子删除
particle.destroy();
&#125;
&#125;</p>
</li>
</ul>
<p><strong>结尾：</strong></p>
<p><strong>ThingJS面向物联网的3D可视化开发平台</strong>拥有强大的物联网开发逻辑，ThingJS 为可视化应用提供了简单、丰富的功能，只需要具有基本的 Javascript 开发经验即可上手。使用者通过接入平台api，轻松集成3D可视化界面，场景搭建-在线开发-数据对接-项目部署，让开发更高效！</p></div>  
</div>
            