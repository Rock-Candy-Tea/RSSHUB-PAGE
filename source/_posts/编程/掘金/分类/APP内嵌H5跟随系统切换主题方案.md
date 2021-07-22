
---
title: 'APP内嵌H5跟随系统切换主题方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59bf90b04df4bf3915c3923bfa9733a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 02:00:27 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59bf90b04df4bf3915c3923bfa9733a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>案例场景：</strong></p>
<p>近日我司app需要实现跟随系统切换主题方案，需要排期(jiaban)实现</p>
<p><strong>实现分析：</strong></p>
<p>1、css变量 var实现主题切换</p>
<p>2、和app交互获取当前主题</p>
<p><strong>按照规矩先：举栗子</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b59bf90b04df4bf3915c3923bfa9733a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用时：</p>
<p>方法的第一个参数是要替换的自定义属性的名称。函数的可选第二个参数用作回退值。如果第一个参数引用的自定义属性无效，则该函数将使用第二个值。</p>
<pre><code class="copyable">/* 在父元素样式中定义一个值 */
.component &#123;
  --text-color: #080; /* header-color 并没有被设定 */
&#125;

/* 在 component 的样式中使用它： */
.component .text &#123;
  color: var(--text-color, black); /* 此处 color 正常取值 --text-color */
&#125;
.component .header &#123;
  color: var(--header-color, blue); /* 此处 color 被回退到 blue */
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>其实就是如果第一个值没有检测到定义过就用第二值，类似于 <strong>let a = b || 1</strong></p>
</blockquote>
<p>我简单做了个demo，供大家参考。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64be8f2efaa64af0a220e6387ec35586~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>效果如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85637aa21ef549ca84314675d95c3713~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>里面的 <strong>:root</strong> 定义可以放在base.less里面，demo指示参考实现</p>
<p>remark：附上代码</p>
<pre><code class="copyable"><template>  <div class="loginPage">    <p class="text">夜见</p>    <div class="btns">      <van-button color="#999999" hairline type="primary" @click="changeTheme('white')">白色主题</van-button>      <van-button color="#191919" hairline type="primary" @click="changeTheme('black')">暗黑模式</van-button>    </div>  </div></template><script setup>// 切换主题const changeTheme = (theme) => &#123;  document.documentElement.dataset.theme = theme&#125;</script><style lang="less" scoped>.loginPage &#123;  padding-top: 10px;  .btns &#123;    display: flex;    justify-content: space-between;    padding: 10px 20px;    box-sizing: border-box;  &#125;&#125;</style><style lang="less">:root &#123;  --primary: #ffffff;  --text-color: #343a40;  --border-color: #343a40;&#125;:root[data-theme='white'] &#123;  --primary: #ffffff;  --text-color: #343a40;  --border-color: #343a40;&#125;:root[data-theme='black'] &#123;  --primary: #343a40;  --text-color: #f8f9fa;  --border-color: #e9ecef;&#125;html,body &#123;  background-color: var(--primary);  height: 100%;  width: 100%;  overscroll-behavior-y: none;&#125;.text &#123;  font-size: 20px;  margin: 0 20px;  padding: 10px;  border-radius: 4px;  color: var(--text-color);  border: 2px solid var(--border-color);&#125;</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            