
---
title: 'Angular _ 在service中使用TemplateRef'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9df33a87d804aad9909e6bc922f96ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Sat, 17 Sep 2022 00:33:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9df33a87d804aad9909e6bc922f96ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>code repo <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frick-chou%2Fangular-demo%2Ftree%2Fmain%2Fhtml-in-service" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rick-chou/angular-demo/tree/main/html-in-service" ref="nofollow noopener noreferrer">github.com/rick-chou/a…</a></p>
</blockquote>
<blockquote>
<p>背景：我希望封装一个自己的 message service 但是我不知道如何在 service 中使用 html 以下是我的一个解决方案</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9df33a87d804aad9909e6bc922f96ea~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="html-in-css" loading="lazy" referrerpolicy="no-referrer"></p>
<p>因为我使用的 NG-ZORRO 的 Notification 组件来做 UI 层</p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fng.ant.design%2Fcomponents%2Fnotification%2Fen" target="_blank" rel="nofollow noopener noreferrer" title="https://ng.ant.design/components/notification/en" ref="nofollow noopener noreferrer">ng.ant.design/components/…</a></p>
</blockquote>
<p><code>NzNotificationService.template</code> 签名如下</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-built_in">template</span>(template: TemplateRef<&#123;&#125;>, options?: NzNotificationDataOptions): NzNotificationRef;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以我需要自定义的 TemplateRef 来满足我的需求</p>
<h3 data-id="heading-0">思路一</h3>
<p>可以在 service 中定义方法 从业务组件中传入 但是这样和直接在业务中使用 <code>NzNotificationService.template</code> 没有什么区别 也就没有集中处理的必要了</p>
<h3 data-id="heading-1">思路二</h3>
<p>给 service 注入 html template</p>
<p>既然不能直接在 service 中书写 html 相关代码 那就沿用思路一的方法</p>
<p>只不过事先在一处与业务无关的地方调用初始化的方法</p>
<p>利用 <code>ng-template</code> 不会生成真实的 dom 节点 以及 service 是全局共享 这两个特性三 我们就可以写出如下代码</p>
<h4 data-id="heading-2">message.service.ts</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Injectable</span>, <span class="hljs-title class_">TemplateRef</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">NzNotificationService</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'ng-zorro-antd/notification'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">enum</span> <span class="hljs-title class_">EMessageCode</span> &#123;
  <span class="hljs-title class_">XXXError</span> = <span class="hljs-number">1024</span>,
  <span class="hljs-title class_">YYYError</span> = <span class="hljs-number">1025</span>,
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">MESSAGE</span> = &#123;
  [<span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">XXXError</span>]: <span class="hljs-string">'XXXError...'</span>,
  [<span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">YYYError</span>]: <span class="hljs-string">'YYYError...'</span>,
&#125;;

<span class="hljs-meta">@Injectable</span>(&#123;
  <span class="hljs-attr">providedIn</span>: <span class="hljs-string">'root'</span>,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">MessageService</span> &#123;
  <span class="hljs-keyword">private</span> templateMap = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Map</span><<span class="hljs-title class_">EMessageCode</span>, <span class="hljs-title class_">TemplateRef</span><<span class="hljs-built_in">any</span>>>();
  <span class="hljs-title function_">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> notificationService: NzNotificationService</span>) &#123;&#125;

  <span class="hljs-comment">// 初始化 templateRef</span>
  <span class="hljs-keyword">public</span> <span class="hljs-title function_">initTemplate</span>(<span class="hljs-attr">message</span>: <span class="hljs-title class_">EMessageCode</span>, <span class="hljs-attr">ref</span>: <span class="hljs-title class_">TemplateRef</span><<span class="hljs-built_in">any</span>>): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">templateMap</span>.<span class="hljs-title function_">set</span>(message, ref);
  &#125;

  <span class="hljs-keyword">public</span> <span class="hljs-title function_">showMessage</span>(<span class="hljs-params">messageCode: EMessageCode</span>) &#123;
    <span class="hljs-keyword">switch</span> (messageCode) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">XXXError</span>:
        <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">notificationService</span>.<span class="hljs-title function_">template</span>(<<span class="hljs-title class_">TemplateRef</span><<span class="hljs-built_in">any</span>>><span class="hljs-variable language_">this</span>.<span class="hljs-property">templateMap</span>.<span class="hljs-title function_">get</span>(messageCode), &#123;
          <span class="hljs-attr">nzDuration</span>: <span class="hljs-number">0</span>,
        &#125;);
      <span class="hljs-keyword">case</span> <span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">YYYError</span>: &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-variable language_">this</span>.<span class="hljs-property">notificationService</span>.<span class="hljs-title function_">error</span>(<span class="hljs-string">'YYYError'</span>, <span class="hljs-variable constant_">MESSAGE</span>[<span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">YYYError</span>]);
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">public</span> <span class="hljs-title function_">removeMessage</span>(<span class="hljs-params">messageId?: <span class="hljs-built_in">string</span></span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">notificationService</span>.<span class="hljs-title function_">remove</span>(messageId);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">message-service-virtual-ref.component</h4>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Component</span>, <span class="hljs-title class_">TemplateRef</span>, <span class="hljs-title class_">ViewChild</span>, <span class="hljs-title class_">AfterViewInit</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">EMessageCode</span>, <span class="hljs-title class_">MessageService</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./message.service'</span>;

<span class="hljs-meta">@Component</span>(&#123;
  <span class="hljs-attr">selector</span>: <span class="hljs-string">'app-message-service-virtual-ref'</span>,
  <span class="hljs-attr">template</span>: <span class="hljs-string">`
    <ng-template #xxx_ref>
      <div class="flex w-[90%]">
        <span nz-icon nzType="close-circle" nzTheme="twotone" class="text-lg mr-2"></span>
        <span>
          There are XXXError, you must refer to
          <a class="cursor-pointer underline text-blue-500 hover:underline" target="_black">something</a>
          to check out
        </span>
      </div>
    </ng-template>
  `</span>,
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">MessageServiceVirtualRefComponent</span> <span class="hljs-keyword">implements</span> <span class="hljs-title class_">AfterViewInit</span> &#123;
  <span class="hljs-meta">@ViewChild</span>(<span class="hljs-string">'xxx_ref'</span>) xxxTemplateRef!: <span class="hljs-title class_">TemplateRef</span><<span class="hljs-built_in">any</span>>;

  <span class="hljs-title function_">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> messageService: MessageService</span>) &#123;&#125;

  <span class="hljs-title function_">ngAfterViewInit</span>(): <span class="hljs-built_in">void</span> &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">messageService</span>.<span class="hljs-title function_">initTemplate</span>(<span class="hljs-title class_">EMessageCode</span>.<span class="hljs-property">XXXError</span>, <span class="hljs-variable language_">this</span>.<span class="hljs-property">xxxTemplateRef</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">app.component.html</h4>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">app-message-service-virtual-ref</span>></span><span class="hljs-tag"></<span class="hljs-name">app-message-service-virtual-ref</span>></span> 
<span class="hljs-tag"><<span class="hljs-name">router-outlet</span>></span><span class="hljs-tag"></<span class="hljs-name">router-outlet</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            