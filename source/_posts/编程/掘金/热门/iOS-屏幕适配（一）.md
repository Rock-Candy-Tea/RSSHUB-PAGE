
---
title: 'iOS-屏幕适配（一）'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f8400566c1a465f8744107442cdf077~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 23:27:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f8400566c1a465f8744107442cdf077~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与好文召集令活动，点击查看： <a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
<h3 data-id="heading-0">iOS设备的分辨率和尺寸</h3>
<p>(参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.paintcodeapp.com%2Fnews%2Fultimate-guide-to-iphone-resolutions" target="_blank" rel="nofollow noopener noreferrer" title="https://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions" ref="nofollow noopener noreferrer">The Ultimate Guide To iPhone Resolutions</a>)</p>
<h4 data-id="heading-1">分辨率</h4>
<ul>
<li>
<p><strong>点（<code>point</code>）：</strong></p>
<p>开发过程中，所有基于坐标系的绘制都以<code>point</code>为单位，<code>point</code>和屏幕上的像素是一一对应的</p>
</li>
<li>
<p><strong>渲染像素（<code>Render Pixels</code>）:</strong></p>
<p>以<code>point</code>为单位绘制最终渲染成<code>pixels</code>，这个过程被称为光栅化，基于<code>point</code>的坐标系乘以比例因子可以得到基于像素的坐标系，高比例因子会使更多的细节展示，目前的比例因子会是<code>1x</code>，<code>2x</code>，<code>3x</code></p>
</li>
<li>
<p><strong>物理像素（<code>Physical Pixels</code>）：</strong></p>
<p>设备屏幕实际像素</p>
</li>
<li>
<p><strong>设备屏幕的物理长度（<code>Physical Device</code>）：</strong></p>
<p>设备的物理长度，使用英寸作为单位，比如<code>iPhone8</code>是<code>4.7</code>英寸，<code>iPhone11</code>是<code>6.1</code>英寸等，这里的数字是指手机屏幕对角线的物理长度，实际上会是<code>Physical Pixels</code>的像素值会渲染到该屏幕，而不是<code>Render Pixels</code>的像素值，屏幕上会有<code>PPI（Pixels-per-inch）</code>的特性，PPI的值告诉你每英寸会有多少像素渲染</p>
</li>
</ul>
<h4 data-id="heading-2">iOS 各个设备对应的分辨率</h4>













































































<table><thead><tr><th align="center">机型</th><th align="center">屏幕宽高(point)</th><th align="center">渲染像素(pixel)</th><th align="center">物理像素(pixel)</th><th align="center">屏幕对角线长度(英寸）</th><th align="center">屏幕模式</th></tr></thead><tbody><tr><td align="center">Phone 5,5s,5c,se</td><td align="center">320 * 568</td><td align="center">640 * 1136</td><td align="center">640 * 1136</td><td align="center">4(326 PPI)</td><td align="center">2x</td></tr><tr><td align="center">Phone 6,6s,7,8</td><td align="center">375 × 667</td><td align="center">750 * 1334</td><td align="center">750 * 1334</td><td align="center">4.7(326PPI)</td><td align="center">2x</td></tr><tr><td align="center">Phone 6p,6sp,7p,8p</td><td align="center">414 * 736</td><td align="center">1242 * 2208</td><td align="center">1080 * 1920</td><td align="center">5.5(401PPI)</td><td align="center">3x</td></tr><tr><td align="center">Phone X,Xs,11Pro</td><td align="center">375 * 812</td><td align="center">1125*2436</td><td align="center">1125*2436</td><td align="center">5.8(458PPI)</td><td align="center">3x</td></tr><tr><td align="center">Phone 11,Xr</td><td align="center">414*896</td><td align="center">828*1792</td><td align="center">828*1792</td><td align="center">6.1(326PPI)</td><td align="center">2x</td></tr><tr><td align="center">Phone 11Pro Max,Xs Max</td><td align="center">414*896</td><td align="center">1242 *2688</td><td align="center">1242 *2688</td><td align="center">6.5(458PPI)</td><td align="center">3x</td></tr><tr><td align="center">iPad 4,5,Air,Air2，mini3，mini4</td><td align="center">1024×768</td><td align="center">2048×1536</td><td align="center">2048×1536</td><td align="center">9.7(264ppi)</td><td align="center">2x</td></tr><tr><td align="center">iPad Pro</td><td align="center">1366*1024</td><td align="center">2732×2048</td><td align="center">2732×2048</td><td align="center">12.9(264ppi)</td><td align="center">2x</td></tr></tbody></table>
<p><strong>屏幕模式（<code>1x</code>, <code>2x</code>, <code>3x</code>）：</strong></p>
<p>描述的就是屏幕中一个点有多少个 <code>Rendered Pixels</code> 渲染，对于<code>2</code>倍屏(又称<code>Retina</code>显示屏)，会有<code>2 * 2 = 4</code> 个像素的面积渲染，对于3倍屏(又称 <code>Retina HD</code> 显示屏)，会有 <code>3 * 3 = 9</code> 个像素的面积渲染</p>
<p>iOS 开发中，所有控件的坐标以及控件大小都是以点为单位的。假如我在屏幕上需要展示一张 20 * 20 (单位：<code>point</code>)大小的图片，那么设计师应该怎么给我图呢？</p>
<p>这里就会用到屏幕模式的概念，如果屏幕是<code>2x</code>，那么就需要提供 <code>40 * 40</code> (单位: <code>pixel</code>)大小的图片，如果屏幕是 <code>3x</code>，那么就提供 <code>60 * 60</code> 大小的图片，且图片的命名需要遵守以下规范:</p>
<pre><code class="hljs language-js copyable" lang="js">Standard:<device_modifier>.<filename_extension>
High resolution:@2x<device_modifier>.<filename_extension>
High HD resolution:@3x<device_modifier>.<filename_extension>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>ImageName: </code></p>
<p>图片名字，根据场景命名
device_modifier: 可选，可以是<code>~ipad</code>或者<code>~iphone</code>, 当需要为 <code>iPad</code> 和 <code>iPhone</code> 分别指定一套图时需要加上此字段
filename_extension: 图片后缀名，<code>iOS</code>中使用<code>png</code>图片</p>
<pre><code class="hljs language-js copyable" lang="js">例如:
MyImage@2x.png - 2x 显示屏自动加载的图片版本
MyImage@3x.png - 3x 显示屏自动加载的图片版本
MyImage@2x~iphone.png - 2x iPhone 和 iPod touch 显示屏自动加载的图片版本
MyImage@3x~iphone.png - 3x iPhone and iPod 显示屏自动加载的图片版本
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-3">设计和开发之间的多屏适配问题</h3>
<p>现在iPhone的屏幕尺寸也不再单一，那么现在以怎样的流程来进行iOS的研发更合适呢？</p>
<h4 data-id="heading-4">基本思路是</h4>
<ul>
<li><strong>选择一种尺寸作为设计和开发基准</strong></li>
<li><strong>定义一套适配规则，自动适配剩下两种尺寸</strong></li>
<li><strong>特殊适配效果给出设计效果</strong></li>
</ul>
<p>这个问题很早之前在知乎上已经被讨论，附上链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttp%3A%2F%2Fwww.zhihu.com%2Fquestion%2F25308946%2Fanswer%2F32240185" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=http://www.zhihu.com/question/25308946/answer/32240185" ref="nofollow noopener noreferrer">手机淘宝设计师pigtwo的回答</a></p>
<h4 data-id="heading-5">多屏适配规范</h4>
<ul>
<li><strong>文字流式</strong></li>
<li><strong>控件弹性</strong></li>
<li><strong>图片等比缩放</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f8400566c1a465f8744107442cdf077~tplv-k3u1fbpfcp-zoom-1.image" alt="多屏适配.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>控件弹性指的是，<code>navigation</code>、<code>cell</code>、<code>bar</code>等适配过程中垂直方向上高度不变；水平方向宽度变化时，通过调整元素间距或元素右对齐的方式实现自适应。这样屏幕越大，在垂直方向上可以显示更多内容，发挥大屏幕的优势</strong></p>
<hr>
<h3 data-id="heading-6">关于xib、storyboard、代码</h3>
<h4 data-id="heading-7">xib和StoryBoard</h4>
<ul>
<li>
<p><code>xib</code>:每个<code>viewcontroller</code>对应单独的<code>xib</code>，可以更加方便单独管理，项目也方便多人一起开发，改动视图方便，不用全局改动</p>
</li>
<li>
<p><code>StoryBoard</code>:<code>StoryBoard</code>是一个包含了多个<code>xib</code>的文件，管理方便，在<code>StoryBoard</code>中不仅可以看到每个<code>ViewController</code>的布局样式，也可以知道各个<code>ViewController</code>之间的转换关系</p>
</li>
<li>
<p>区别</p>
<ul>
<li>项目大的话，<code>xib</code>文件过多，不容易统一管理。跳转只能在代码实现，比较混乱</li>
<li><code>StoryBoard</code>适合单独开发并且是中小型项目的时候使用</li>
</ul>
</li>
</ul>
<h4 data-id="heading-8">xib和代码区别</h4>
<ul>
<li>
<p><code>xib</code>优缺点</p>
<ul>
<li><code>xib</code>可视化，开发速度快，代码量少</li>
<li>合作开发，彼此阅读困难，无法在<code>git</code>上查看历史改动，容易造成冲突，造成冲突后难以解决，容易产生不必要的<code>commit</code></li>
<li>性能上，<code>xib</code>加载慢，打开速度也慢，而且会占用app包的体积</li>
</ul>
</li>
<li>
<p>代码优缺点</p>
<ul>
<li>灵活，方便，所有的属性都可以通过代码来控制，简单来说，<code>xib</code>能做的，纯代码都能做而他们不能做的，纯代码也能做</li>
<li>对大型项目、团队开发都很友好，尤其是在版本控制，代码管理方面。唯一的缺点就是繁琐以及代码量大</li>
</ul>
</li>
</ul>
<h3 data-id="heading-9">常见布局方式</h3>
<ul>
<li>固定间距 ：不同尺寸下，间距总是固定的</li>
<li>流式布局 ： 文字、图片等在不同屏幕下流式排布，比如大屏下一行显示四张图片，小屏一行三张，图片尺寸固定</li>
<li>比例放大 ：间距、文字大小，图片大小等比例放大</li>
<li>保持比值 ：俩个UI元素或者图片的长宽等属性保持一定的比值</li>
<li>对齐 ：元素间按某个方向对齐</li>
</ul>
<h3 data-id="heading-10">常见布局屏幕适配的方式</h3>
<ul>
<li>
<p><a href="https://juejin.cn/post/6983179458559606797" target="_blank" title="https://juejin.cn/post/6983179458559606797">Autoresizing</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6983861948664250382" target="_blank" title="https://juejin.cn/post/6983861948664250382">AutoLayou</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6985332589431259143" target="_blank" title="https://juejin.cn/post/6985332589431259143">VFL</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6986475724265766949" target="_blank" title="https://juejin.cn/post/6986475724265766949">Masonry</a></p>
</li>
<li>
<p><a href="https://juejin.cn/post/6979390190192164878" target="_blank" title="https://juejin.cn/post/6979390190192164878">SnapKit</a></p>
</li>
</ul></div>  
</div>
            