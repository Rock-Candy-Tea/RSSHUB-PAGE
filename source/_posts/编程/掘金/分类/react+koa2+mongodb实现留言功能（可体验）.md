
---
title: 'react+koa2+mongodb实现留言功能（可体验）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89efd876f46e410a84215b5551f0488f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 16:19:07 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89efd876f46e410a84215b5551f0488f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>留言功能</strong>在社交中占据很重要的作用。这里实现的留言功能，参考微信朋友圈的方式：</p>
<blockquote>
<p>用户发送一个<code>TOPIC</code>话题，读者可以在该话题下面进行评论，也可以对该话题下的留言进行评论。但是始终只会展示两层树的评论。</p>
</blockquote>
<blockquote>
<p>当然，也可以像掘金这样进行嵌套多层树的结构展示。臣妾觉得嵌套得太深~</p>
</blockquote>
<p>实际完成的效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89efd876f46e410a84215b5551f0488f~tplv-k3u1fbpfcp-watermark.image" alt="global_leave_message.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>体验站点请戳 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjimmyarea.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jimmyarea.com/" ref="nofollow noopener noreferrer">jimmyarea.com</a> 。</p>
<h3 data-id="heading-0">前端实现</h3>
<p>使用技术</p>
<ul>
<li>
<p>react</p>
</li>
<li>
<p>ant design</p>
</li>
<li>
<p>typescript</p>
</li>
</ul>
<p>在上面的截图中，很明显，就是一个表单的设计，外加一个列表的展示。</p>
<p>表单的设计使用了<code>ant design</code>框架自带的<code>form</code>组件：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><Form
  &#123;...layout&#125;
  form=&#123;form&#125;
  name=<span class="hljs-string">"basic"</span>
  onFinish=&#123;onFinish&#125;
  onFinishFailed=&#123;onFinishFailed&#125;
>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span>
    <span class="hljs-attr">label</span>=<span class="hljs-string">"主题"</span>
    <span class="hljs-attr">name</span>=<span class="hljs-string">"subject"</span>
    <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
      &#123; <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '请输入你的主题' &#125;,
      &#123; <span class="hljs-attr">whitespace:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '输入不能为空' &#125;,
      &#123; <span class="hljs-attr">min:</span> <span class="hljs-attr">6</span>, <span class="hljs-attr">message:</span> '主题不能小于<span class="hljs-attr">6</span>个字符' &#125;,
      &#123; <span class="hljs-attr">max:</span> <span class="hljs-attr">30</span>, <span class="hljs-attr">message:</span> '主题不能大于<span class="hljs-attr">30</span>个字符' &#125;,
    ]&#125;
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">Input</span> <span class="hljs-attr">maxLength</span>=<span class="hljs-string">&#123;30&#125;</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入你的主题（最少6字符，最多30字符）"</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>

  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span>
    <span class="hljs-attr">label</span>=<span class="hljs-string">"内容"</span>
    <span class="hljs-attr">name</span>=<span class="hljs-string">"content"</span>
    <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
      &#123; <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '请输入你的内容' &#125;,
      &#123; <span class="hljs-attr">whitespace:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '输入不能为空' &#125;,
      &#123; <span class="hljs-attr">min:</span> <span class="hljs-attr">30</span>, <span class="hljs-attr">message:</span> '内容不能小于<span class="hljs-attr">30</span>个字符' &#125;,
    ]&#125;
  ></span>
    <span class="hljs-tag"><<span class="hljs-name">Input.TextArea</span>
      <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"请输入你的内容（最少30字符）"</span>
      <span class="hljs-attr">autoSize</span>=<span class="hljs-string">&#123;&#123;</span>
        <span class="hljs-attr">minRows:</span> <span class="hljs-attr">6</span>,
        <span class="hljs-attr">maxRows:</span> <span class="hljs-attr">12</span>,
      &#125;&#125;
      <span class="hljs-attr">showCount</span>
      <span class="hljs-attr">maxLength</span>=<span class="hljs-string">&#123;300&#125;</span>
    /></span>
  <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Form.Item</span> &#123;<span class="hljs-attr">...tailLayout</span>&#125;></span>
    <span class="hljs-tag"><<span class="hljs-name">Button</span>
      <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
      <span class="hljs-attr">htmlType</span>=<span class="hljs-string">"submit"</span>
      <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> '<span class="hljs-attr">100</span>%' &#125;&#125;
      <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;loading&#125;</span>
      <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;loading&#125;</span>
    ></span>
      <span class="hljs-tag"><<span class="hljs-name">CloudUploadOutlined</span> /></span>
      <span class="hljs-symbol">&nbsp;</span>Submit
    <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span></span>
</Form>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里限制了输入的主题名称的长度为6-30；内容是30-300字符</p>
</blockquote>
<p>针对留言的展示，这里使用的是<code>ant design</code>自带的<code>List</code>和<code>Comment</code>组件：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><List
  loading=&#123;loadingMsg&#125;
  itemLayout=<span class="hljs-string">"horizontal"</span>
  pagination=&#123;&#123;
    <span class="hljs-attr">size</span>: <span class="hljs-string">'small'</span>,
    <span class="hljs-attr">total</span>: count,
    <span class="hljs-attr">showTotal</span>: <span class="hljs-function">() =></span> <span class="hljs-string">`共 <span class="hljs-subst">$&#123;count&#125;</span> 条`</span>,
    pageSize,
    <span class="hljs-attr">current</span>: activePage,
    <span class="hljs-attr">onChange</span>: changePage,
  &#125;&#125;
  dataSource=&#123;list&#125;
  renderItem=&#123;<span class="hljs-function">(<span class="hljs-params">item: <span class="hljs-built_in">any</span>, index: <span class="hljs-built_in">any</span></span>) =></span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">List.Item</span> <span class="hljs-attr">actions</span>=<span class="hljs-string">&#123;[]&#125;</span> <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;index&#125;</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">List.Item.Meta</span>
        <span class="hljs-attr">avatar</span>=<span class="hljs-string">&#123;</span>
          <<span class="hljs-attr">Avatar</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> '#<span class="hljs-attr">1890ff</span>' &#125;&#125;></span>
            &#123;item.userId?.username?.slice(0, 1)?.toUpperCase()&#125;
          <span class="hljs-tag"></<span class="hljs-name">Avatar</span>></span>
        &#125;
        title=&#123;<span class="hljs-tag"><<span class="hljs-name">b</span>></span>&#123;item.subject&#125;<span class="hljs-tag"></<span class="hljs-name">b</span>></span>&#125;
        description=&#123;
          <span class="hljs-tag"><></span>
            &#123;item.content&#125;
            &#123;/* 子留言 */&#125;
            <span class="hljs-tag"><<span class="hljs-name">div</span>
              <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
                <span class="hljs-attr">fontSize:</span> '<span class="hljs-attr">12px</span>',
                <span class="hljs-attr">marginTop:</span> '<span class="hljs-attr">8px</span>',
                <span class="hljs-attr">marginBottom:</span> '<span class="hljs-attr">16px</span>',
                <span class="hljs-attr">alignItems:</span> '<span class="hljs-attr">center</span>',
                <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>',
                <span class="hljs-attr">flexWrap:</span> '<span class="hljs-attr">wrap</span>',
                <span class="hljs-attr">justifyContent:</span> '<span class="hljs-attr">space-between</span>',
              &#125;&#125;
            ></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
                用户<span class="hljs-symbol">&nbsp;</span>&#123;item.userId?.username&#125;<span class="hljs-symbol">&nbsp;</span><span class="hljs-symbol">&nbsp;</span>发表于<span class="hljs-symbol">&nbsp;</span>
                &#123;moment(item.meta?.createAt).format('YYYY-MM-DD HH:mm:ss')&#125;
              <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span>></span>
                &#123;item.canDel ? (
                  <span class="hljs-tag"><<span class="hljs-name">a</span>
                    <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">color:</span> '<span class="hljs-attr">red</span>', <span class="hljs-attr">fontSize:</span> '<span class="hljs-attr">12px</span>', <span class="hljs-attr">marginRight:</span> '<span class="hljs-attr">12px</span>' &#125;&#125;
                    <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> removeMsg(item)&#125;
                  >
                    <span class="hljs-tag"><<span class="hljs-name">DeleteOutlined</span> /></span>
                    <span class="hljs-symbol">&nbsp;</span> Delete
                  <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
                ) : null&#125;
                <span class="hljs-tag"><<span class="hljs-name">a</span>
                  <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">fontSize:</span> '<span class="hljs-attr">12px</span>', <span class="hljs-attr">marginRight:</span> '<span class="hljs-attr">12px</span>' &#125;&#125;
                  <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> replyMsg(item)&#125;
                >
                  <span class="hljs-tag"><<span class="hljs-name">MessageOutlined</span> /></span>
                  <span class="hljs-symbol">&nbsp;</span> Reply
                <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            &#123;/* 回复的内容 */&#125;
            &#123;item.children && item.children.length ? (
              <span class="hljs-tag"><></span>
                &#123;item.children.map((innerItem: any, innerIndex: any) => (
                  <span class="hljs-tag"><<span class="hljs-name">Comment</span>
                    <span class="hljs-attr">key</span>=<span class="hljs-string">&#123;innerIndex&#125;</span>
                    <span class="hljs-attr">author</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">span</span>></span>&#123;innerItem.subject&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>&#125;
                    avatar=&#123;
                      <span class="hljs-tag"><<span class="hljs-name">Avatar</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">backgroundColor:</span> '#<span class="hljs-attr">1890ff</span>' &#125;&#125;></span>
                        &#123;innerItem.userId?.username?.slice(0, 1)?.toUpperCase()&#125;
                      <span class="hljs-tag"></<span class="hljs-name">Avatar</span>></span>
                    &#125;
                    content=&#123;<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;innerItem.content&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>&#125;
                    datetime=&#123;
                      <span class="hljs-tag"><<span class="hljs-name">Tooltip</span>
                        <span class="hljs-attr">title</span>=<span class="hljs-string">&#123;moment(innerItem.meta?.createAt).format(</span>
                          '<span class="hljs-attr">YYYY-MM-DD</span> <span class="hljs-attr">HH:mm:ss</span>',
                        )&#125;
                      ></span>
                        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;moment(innerItem.meta?.createAt).fromNow()&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                      <span class="hljs-tag"></<span class="hljs-name">Tooltip</span>></span>
                    &#125;
                    actions=&#123;[
                      <span class="hljs-tag"><></span>
                        &#123;innerItem.canDel ? (
                          <span class="hljs-tag"><<span class="hljs-name">a</span>
                            <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span>
                              <span class="hljs-attr">color:</span> '<span class="hljs-attr">red</span>',
                              <span class="hljs-attr">fontSize:</span> '<span class="hljs-attr">12px</span>',
                              <span class="hljs-attr">marginRight:</span> '<span class="hljs-attr">12px</span>',
                            &#125;&#125;
                            <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> removeMsg(innerItem)&#125;
                          >
                            <span class="hljs-tag"><<span class="hljs-name">DeleteOutlined</span> /></span>
                            <span class="hljs-symbol">&nbsp;</span> Delete
                          <span class="hljs-tag"></<span class="hljs-name">a</span>></span>
                        ) : null&#125;
                      <span class="hljs-tag"></></span>,
                      <span class="hljs-tag"><<span class="hljs-name">a</span>
                        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">fontSize:</span> '<span class="hljs-attr">12px</span>', <span class="hljs-attr">marginRight:</span> '<span class="hljs-attr">12px</span>' &#125;&#125;
                        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> replyMsg(innerItem)&#125;
                      >
                        <span class="hljs-tag"><<span class="hljs-name">MessageOutlined</span> /></span>
                        <span class="hljs-symbol">&nbsp;</span> Reply
                      <span class="hljs-tag"></<span class="hljs-name">a</span>></span>,
                    ]&#125;
                  />
                ))&#125;
              <span class="hljs-tag"></></span></span>
            ) : <span class="hljs-literal">null</span>&#125;

            &#123;<span class="hljs-comment">/* 回复的表单 */</span>&#125;
            &#123;replyObj._id === item._id || replyObj.pid === item._id ? (
              <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginTop:</span> '<span class="hljs-attr">12px</span>' &#125;&#125; <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;replyArea&#125;</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">Form</span>
                  <span class="hljs-attr">form</span>=<span class="hljs-string">&#123;replyForm&#125;</span>
                  <span class="hljs-attr">name</span>=<span class="hljs-string">"reply"</span>
                  <span class="hljs-attr">onFinish</span>=<span class="hljs-string">&#123;onFinishReply&#125;</span>
                  <span class="hljs-attr">onFinishFailed</span>=<span class="hljs-string">&#123;onFinishFailed&#125;</span>
                ></span>
                  <span class="hljs-tag"><<span class="hljs-name">Form.Item</span>
                    <span class="hljs-attr">name</span>=<span class="hljs-string">"reply"</span>
                    <span class="hljs-attr">rules</span>=<span class="hljs-string">&#123;[</span>
                      &#123; <span class="hljs-attr">required:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '请输入你的内容' &#125;,
                      &#123; <span class="hljs-attr">whitespace:</span> <span class="hljs-attr">true</span>, <span class="hljs-attr">message:</span> '输入不能为空' &#125;,
                      &#123; <span class="hljs-attr">min:</span> <span class="hljs-attr">2</span>, <span class="hljs-attr">message:</span> '内容不能小于<span class="hljs-attr">2</span>个字符' &#125;,
                    ]&#125;
                  ></span>
                    <span class="hljs-tag"><<span class="hljs-name">Input.TextArea</span>
                      <span class="hljs-attr">placeholder</span>=<span class="hljs-string">&#123;replyPlaceholder&#125;</span>
                      <span class="hljs-attr">autoSize</span>=<span class="hljs-string">&#123;&#123;</span>
                        <span class="hljs-attr">minRows:</span> <span class="hljs-attr">6</span>,
                        <span class="hljs-attr">maxRows:</span> <span class="hljs-attr">12</span>,
                      &#125;&#125;
                      <span class="hljs-attr">showCount</span>
                      <span class="hljs-attr">maxLength</span>=<span class="hljs-string">&#123;300&#125;</span>
                    /></span>
                  <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span>

                  <span class="hljs-tag"><<span class="hljs-name">Form.Item</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">flex</span>', <span class="hljs-attr">justifyContent:</span> '<span class="hljs-attr">flex-end</span>' &#125;&#125;></span>
                      <span class="hljs-tag"><<span class="hljs-name">Button</span>
                        <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">marginRight:</span> '<span class="hljs-attr">12px</span>' &#125;&#125;
                        <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> cancelReply()&#125;
                      >
                        Dismiss
                      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                      <span class="hljs-tag"><<span class="hljs-name">Button</span>
                        <span class="hljs-attr">type</span>=<span class="hljs-string">"primary"</span>
                        <span class="hljs-attr">htmlType</span>=<span class="hljs-string">"submit"</span>
                        <span class="hljs-attr">loading</span>=<span class="hljs-string">&#123;innerLoading&#125;</span>
                        <span class="hljs-attr">disabled</span>=<span class="hljs-string">&#123;innerLoading&#125;</span>
                      ></span>
                        Submit
                      <span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
                  <span class="hljs-tag"></<span class="hljs-name">Form.Item</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">Form</span>></span>
              <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
            ) : <span class="hljs-literal">null</span>&#125;
          </>
        &#125;
      />
    </List.Item>
  )&#125;
/>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当然，如果是多级地树结构嵌套，你完全可以只是使用<code>Comment</code>组件进行递归调用</p>
</blockquote>
<p>列表是对用户发表的主题，留言以及子留言的展示。如果你纵览上面的代码片段，你会发现里面有一个<code>Form</code>表单。</p>
<p>是的，其<code>Form</code>表单就是给留言使用的，其结构仅仅是剔除了主题留言中的<code>subject</code>字段输入框，但是实际传参我还是会使用到。</p>
<p>完整的前端代码可前往<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freng99%2Fblogs%2Fwiki%2Fjimmyarea-%25E7%2595%2599%25E8%25A8%2580%25EF%25BC%2588%25E5%2589%258D%25E7%25AB%25AF%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reng99/blogs/wiki/jimmyarea-%E7%95%99%E8%A8%80%EF%BC%88%E5%89%8D%E7%AB%AF%EF%BC%89" ref="nofollow noopener noreferrer">jimmyarea 留言（前端）</a>查看。</p>
<h3 data-id="heading-1">后端</h3>
<p>使用的技术：</p>
<ul>
<li>
<p>mongodb 数据库，这里我使用到了其ODM <code>mongoose</code></p>
</li>
<li>
<p>koa2 一个<code>Node</code>框架</p>
</li>
<li>
<p>pm2 进程守卫</p>
</li>
<li>
<p>apidoc 用来生成接口文档（如果你留意<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjimmyarea.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jimmyarea.com/" ref="nofollow noopener noreferrer">体验站点</a>，右上角有一个"文档"的链接，链接的内容就是生成的文档内容）</p>
</li>
</ul>
<p>这里的搭建就不进行介绍了，可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fkoa.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://koa.bootcss.com/" ref="nofollow noopener noreferrer">koa2官网</a>配合百度解决~</p>
<p>其实，本质上还是增删改查的操作。</p>
<p>首先，我们对自己要存储的数据结构<code>schema</code>进行相关的定义：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> mongoose = <span class="hljs-built_in">require</span>(<span class="hljs-string">'mongoose'</span>)
<span class="hljs-keyword">const</span> Schema = mongoose.Schema

<span class="hljs-comment">// 定义留言字段</span>
<span class="hljs-keyword">let</span> MessageSchema = <span class="hljs-keyword">new</span> Schema(&#123;
  <span class="hljs-comment">// 关联字段 -- 用户的id</span>
  <span class="hljs-attr">userId</span>: &#123;
    <span class="hljs-attr">type</span>: mongoose.Schema.Types.ObjectId,
    <span class="hljs-attr">ref</span>: <span class="hljs-string">'User'</span>
  &#125;,
  <span class="hljs-attr">type</span>: <span class="hljs-built_in">Number</span>, <span class="hljs-comment">// 1是留言，2是回复</span>
  <span class="hljs-attr">subject</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">// 留言主题 </span>
  <span class="hljs-attr">content</span>: <span class="hljs-built_in">String</span>, <span class="hljs-comment">//  留言内容</span>
  <span class="hljs-attr">pid</span>: &#123; <span class="hljs-comment">// 父id</span>
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'-1'</span>
  &#125;,
  <span class="hljs-attr">replyTargetId</span>: &#123; <span class="hljs-comment">// 回复目标记录id， 和父pid有所不同</span>
    <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
    <span class="hljs-attr">default</span>: <span class="hljs-string">'-1'</span>
  &#125;,
  <span class="hljs-attr">meta</span>: &#123;
    <span class="hljs-attr">createAt</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Date</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-built_in">Date</span>.now()
    &#125;,
    <span class="hljs-attr">updateAt</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Date</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-built_in">Date</span>.now()
    &#125;
  &#125;
&#125;)

mongoose.model(<span class="hljs-string">'Message'</span>, MessageSchema)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有个注意的点<code>userId</code>字段，这里我直接关联了注册的用户。</p>
<p>完成了字段的设定之后，下面就可以进行增删改查了。</p>
<p>详细的<code>crud</code>代码可以到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freng99%2Fblogs%2Fwiki%2Fjimmyarea-%25E7%2595%2599%25E8%25A8%2580%25EF%25BC%2588%25E5%2590%258E%25E7%25AB%25AF%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reng99/blogs/wiki/jimmyarea-%E7%95%99%E8%A8%80%EF%BC%88%E5%90%8E%E7%AB%AF%EF%BC%89" ref="nofollow noopener noreferrer">jimmyarea 留言（后端）</a> 查看。</p>
<p><strong>本篇的重点是，对评论的话题和留言，如何转换成两层的树型结构呢？</strong></p>
<p>这就是涉及到了<code>pid</code>这个字段，也就是<code>父节点的id</code>: 话题的<code>pid</code>为<code>-1</code>，话题下留言的<code>pid</code>为话题的记录值。如下代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> count = <span class="hljs-keyword">await</span> Message.count(&#123;<span class="hljs-attr">pid</span>: <span class="hljs-string">'-1'</span>&#125;)
<span class="hljs-keyword">let</span> data = <span class="hljs-keyword">await</span> Message.find(&#123;<span class="hljs-attr">pid</span>: <span class="hljs-string">'-1'</span>&#125;)
                      .skip((current-<span class="hljs-number">1</span>) * pageSize)
                      .limit(pageSize)
                      .sort(&#123; <span class="hljs-string">'meta.createAt'</span>: -<span class="hljs-number">1</span>&#125;)
                      .populate(&#123;
                        <span class="hljs-attr">path</span>: <span class="hljs-string">'userId'</span>,
                        <span class="hljs-attr">select</span>: <span class="hljs-string">'username _id'</span> <span class="hljs-comment">// select: 'username -_id' -_id 是排除_id</span>
                      &#125;)
                      .lean(<span class="hljs-literal">true</span>) <span class="hljs-comment">// 添加lean变成js的json字符串</span>

<span class="hljs-keyword">const</span> pids = <span class="hljs-built_in">Array</span>.isArray(data) ? data.map(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i._id) : [];
<span class="hljs-keyword">let</span> resReply = []
<span class="hljs-keyword">if</span>(pids.length) &#123;
resReply = <span class="hljs-keyword">await</span> Message.find(&#123;<span class="hljs-attr">pid</span>: &#123;<span class="hljs-attr">$in</span>: pids&#125;&#125;)
                               .sort(&#123; <span class="hljs-string">'meta.createAt'</span>: <span class="hljs-number">1</span>&#125;)
                               .populate(&#123;
                                <span class="hljs-attr">path</span>: <span class="hljs-string">'userId'</span>,
                                <span class="hljs-attr">select</span>: <span class="hljs-string">'username _id'</span> <span class="hljs-comment">// select: 'username -_id' -_id 是排除_id</span>
                              &#125;)
&#125;

<span class="hljs-keyword">const</span> list = data.map(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
<span class="hljs-keyword">const</span> children = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(resReply.filter(<span class="hljs-function"><span class="hljs-params">i</span> =></span> i.pid === item._id.toString()))) <span class="hljs-comment">// 引用问题</span>
<span class="hljs-keyword">const</span> tranformChildren = children.map(<span class="hljs-function"><span class="hljs-params">innerItem</span> =></span> (&#123;
  ...innerItem,
  <span class="hljs-attr">canDel</span>: innerItem.userId && innerItem.userId._id.toString() === (user._id&&user._id.toString()) ? <span class="hljs-number">1</span> : <span class="hljs-number">0</span>
&#125;))
<span class="hljs-keyword">return</span> &#123;
  ...item,
  <span class="hljs-attr">children</span>: tranformChildren,
  <span class="hljs-attr">canDel</span>: item.userId && item.userId._id.toString() === (user._id&&user._id.toString()) ? <span class="hljs-number">1</span> : <span class="hljs-number">0</span>
&#125;
&#125;)

<span class="hljs-keyword">if</span>(list) &#123;
  ctx.body = &#123;
    <span class="hljs-attr">results</span>: list,
    <span class="hljs-attr">current</span>: <span class="hljs-number">1</span>,
    count
  &#125;
  <span class="hljs-keyword">return</span>
&#125;
ctx.body = &#123;
  <span class="hljs-attr">code</span>: <span class="hljs-number">10002</span>,
  <span class="hljs-attr">msg</span>: <span class="hljs-string">'获取留言失败！'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，可以愉快地进行留言~</p>
<h3 data-id="heading-2">后话</h3>
<ul>
<li>
<p>更多内容可前往 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freng99" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reng99" ref="nofollow noopener noreferrer">jimmy github</a></p>
</li>
<li>
<p>留言的关键代码可前往 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freng99%2Fblogs%2Fwiki" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reng99/blogs/wiki" ref="nofollow noopener noreferrer">jimmy 留言功能</a></p>
</li>
<li>
<p>留言的体验地址可前往 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fjimmyarea.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jimmyarea.com/" ref="nofollow noopener noreferrer">jimmyarea.com</a></p>
</li>
</ul></div>  
</div>
            