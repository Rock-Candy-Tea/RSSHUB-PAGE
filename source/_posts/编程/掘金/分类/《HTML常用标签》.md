
---
title: '《HTML常用标签》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cffd04ab9605498c92433d3dd806feab~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 16 Apr 2021 23:44:55 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cffd04ab9605498c92433d3dd806feab~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style>


    
    
    
    HTML常用标签

<h2 data-id="heading-0">HTML常用标签</h2>
测试2

    <div>
    
    <dl><ol><h3 data-id="heading-1">常用的标签：</h3>
        <dt><strong><li><code>a</code> 标签的用法</li></strong></dt>
            <dd><code>a</code> 标签的作用
                <ul>
                <li>跳转到外部页面。</li>
                <li>跳转到内部锚点</li>
                <li>跳转到邮箱或者电话等</li><hr>
                </ul>
                <code>a</code> 标签常用的属性
                <ul type="disc">
                <li><code>href</code>——>超链接，链接到某个网页。</li>
                <ul type="circle"><code>a</code>的<code>href</code>的取值
                    <li>网址</li>
                        <ul>
                            <li>https://google.com</li>
                            <li>http://google.com</li>
                            前两个为有协议访问
                            <li>//google.com</li>
                            此为无限已访问，最高级，会自动跳转
                        </ul>
                    <li>路径</li>
                        <ul>
                            <li><code>/a/b/c</code>以及<code>a/b/c</code></li>
                            <li><code>index.html</code>以及<code>./index.html</code></li>
                        </ul>
                    <li>伪协议</li>
                        <ul>
                            <li>javascript:代码;</li>
                            <li>mailto:邮箱</li>
                            <li>tel:手机号</li>
                            可自动跳转到指定标签，自动填写邮箱或者手机号，用户只需确认即可。
                        </ul>
                </ul><hr>
                <li><code>target</code>——>指定在哪个窗口打开超链接。</li>
                <ul type="circle"><code>a</code>的<code>target</code>的取值
                    <li>内置名字</li>
                        <ul>
                            <li><code>_blank</code>——>在新建的空白页面打开。</li>
                            <li><code>_top</code>——>在(多内嵌页面)最顶层页面打开。</li>
                            <li><code>_parent</code>——>在父亲窗口页面打开，即当层页面上一层。</li>
                            <li><code>_self</code>——>其实是默认值，在当前页面打开。</li>
                            这是个多层嵌套示例
<p><img alt="target.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cffd04ab9605498c92433d3dd806feab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
</p></ul>
<li>程序员命名</li>
常与后续JS结合使用，下面介绍作用。
<ul>
<li><code>windows</code>的<code>name</code></li>
若已有命名<code>windows.name</code>><code>xxx</code>，则在<code>xxx</code>窗口打开页面。若没有命名为<code>xxx</code>页面，则<code>windows.name</code>新建<code>xxx</code>页面后，再在此页面打开。
<li><code>iframe</code>的<code>name</code></li>可以指定到<code>iframe</code>命名的页面打开(题外话：可实现goobai页面~！)。
</ul>
</ul><hr>
<li><code>download</code>——>理论上是下载超链接网页。(已不支持，不建议用)</li>
<ul type="circle">
<li>作用</li>
不是打开页面，而是下载页面。
<li>问题</li>
不是所有浏览器都支持，尤其是手机浏览器。
</ul>
<hr>
<li><code>rel=noopener</code>——>防止bug。(JS里有具体的解释)</li>
</ul>
</dd>
<hr>
<dt><strong><li><code>img</code> 标签的用法</li></strong></dt>
<dd><code>img</code> 标签的作用
<ul>
<li>发出一个ge请求，展示一张图片。</li><p></p>
<p><img alt="get.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83fa09d3b1414ef7b6f83913612026e2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p><hr>
</ul>
<code>img</code> 标签常用的属性
<ul>
<li><code>alt</code>——>代替，若<code>src</code>加载失败，则显示<code>alt</code>，后接与<code>src</code>相同。</li>
<li><code>height</code>——>设置图片高度。(只设置高度，宽度则自适应设置)</li>
<li><code>width</code>——>设置图片宽度。(只设置宽度，高度则自适应设置)</li>
<li><code>src</code>——>source的简写，后接图片源地址，可以是网络地址，相对路径和绝对路径。</li>
</ul>
<code>img</code> 在标签JS中的两个重要事件<br>
监听图片是否加载成功。
<ul>
<li>若加载成功则调用<code>onload</code></li>
<li>若加载失败则调用<code>onerror</code></li>
</ul>
作用是：可在图片加载失败的时候进行挽救。<p></p>
<p><img alt="shijian.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059e93b2e327489d9cb174dd921d0439~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p><hr>
<code>img</code> 标签做响应式<br>
<code>max-width: 100%;</code><br>
老古董Iphone5也能浏览全图<p></p>
<p><img alt="iphone5.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06b45efd13124cb3916022aa955ac1a1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p><hr>
<br><code>img</code> 标签是<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/Replaced_element" target="_blank" rel="nofollow noopener noreferrer">可替换元素</a><br>
</dd>
<hr>
<dt><strong><li><code>table</code> 标签的用法</li></strong></dt>
<dd>相关的标签
<ul><code>table</code>标签内常用的只能有<code>thead</code>,<code>tbody</code>,<code>tfoot</code>这三种标签。<br>
t都是table的简写。
<li><code>table</code>——>表格标签</li>
<li><code>thead</code>——>表的头部</li>
<li><code>tbody</code>——>表的驱赶</li>
<li><code>tfoot</code>——>表的尾部</li>
<li><code>tr</code>——>table raw，表的一行</li>
<li><code>td</code>——>table data，表内的数据</li>
<li><code>th</code>——>table head，一列的表头</li>
</ul>
<em>注：若不写前三标签，不按顺序写，浏览器强悍的纠错能力也会自动把代码按顺序完整修改。(习惯不好)</em><br>
示例<p></p>
<pre><code class="hljs language-js copyable" lang="js">    <table>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">thead</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span><span class="hljs-tag"></<span class="hljs-name">th</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span>小明<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span>小红<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">thead</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">tbody</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span>语文<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>98<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>95<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span>数学<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>94<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>99<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">tbody</span>></span></span>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">tfoot</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">tr</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">th</span>></span>总分<span class="hljs-tag"></<span class="hljs-name">th</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>192<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">td</span>></span>194<span class="hljs-tag"></<span class="hljs-name">td</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">tr</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">tfoot</span>></span></span>
    </table>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相关的样式
</p><ul>
<li><code>table-layout</code>——>常用有2个设置</li>
<ul>
<li><code>table-layout: auto;</code> 自动表格布局算法对表格布局。表格及单元格的宽度取决于其包含的内容。</li>
<li><code>table-layout: fixed;</code> 表格和列的宽度通过表格的宽度来设置，某一列的宽度仅由首行的单元格决定。</li>
</ul>
<li><code>border-collapse</code>——>单元格边框合并设置。</li>
<li><code>border-spacing</code>——>单元格的边框距离设置。</li>
</ul>
</dd><hr>
<dt><strong><li>其他感想</li></strong></dt>
<dd>几个注意事项
<ul type="disc">
<li>要用http-server或者parcel等之类的工具来预览html文件。这样开启服务端口所在的文件即是根目录。</li>
<li>伪协议<code>javascript:;</code>可以满足什么都不做的a标签。</li>
<li><code>iframe标签</code>内嵌窗口。很少使用了，还有些老系统在使用。(不好用)</li>
<li><code>border-collapse</code>和<code>border-spacing</code>常写到reset.CSS里面。</li>
<li>还有几个常用但是与后续CSS,JS一起理解的标签</li>
<ul type="circle">
<li><code>form</code>标签 表单</li>
<ul>属性
<li><code>actoin</code>——>发出页面请求，控制用那个页面，与后续JS并用。</li>
<li><code>autocomplete</code>——>on/off。根据name值提示输入内容，便于用户输入用户名等。</li>
<li><code>method</code>——>控制用get还是Post请求页面</li>
<li><code>target</code>——>控制要提交到那个页面。</li>
事件
<li><code>onsubmit</code> 提交时触发</li>
</ul>
<li><code>input</code>标签 让用户输入内容</li>
<ul>属性
<li>类型<code>type</code>：<code>button</code>/<code>checkbox</code>/<code>email</code>/<code>file</code>/<code>hidden</code>/<code>color</code>/<code>number</code>/<code>password</code>/<code>radio</code>/<code>search</code>/<code>submit</code>/<code>tel</code>/<code>text</code></li>
其他<li><code>name</code>/<code>autofocus</code>/<code>checked</code>/<code>disabled</code>/<code>maxlength</code>/<code>pattern</code>/<code>value</code>/<code>placedholder</code></li>
事件
<li><code>onchange</code>改写/<code>onfocus</code>聚焦/<code>onblur</code>失焦</li>
注：一般不监听onclick事件，不好用。<br>
验证器
<li>HTML5新增的自带功能。</li>
</ul>
<li>其他输入标签</li>
<ul>
<li><code>select</code>+<code>option</code></li>
<li><code>textarea</code></li>
<li><code>label</code></li>
</ul>
<li>其他标签</li>
<ul>
<li><code>video</code></li>
<li><code>audio</code></li>
<li><code>canvas</code></li>
<li><code>svg</code></li>
</ul>
</ul>
<em>注：这些标签的兼容性一定要查看文档。<br>
这些都是今后结合其他后续课程一起专门学习的。</em>
</ul><hr>
<strong>学习感想</strong><br>
HTML标签多的枯燥，还与后续的课程结合才能加深理解。总结起来就是需要自己亲自写代码，复刻老师或者同学优秀的测试回答。通过之后，不管忘没忘记html，都需要再花更多时间往后学习相关的课程，这些课程都不是独立的，而是相互联系的，分配好时间能充分应对遗忘曲线。
</dd><hr>
</ol></dl>

</div><p></p>

©转载声明<br>
参考资料<br>
<p><a href="https://developer.mozilla.org/zh-CN/docs/conflicting/Web/HTML/Element" target="_blank" rel="nofollow noopener noreferrer">MDN_HTML5</a></p>
</div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            