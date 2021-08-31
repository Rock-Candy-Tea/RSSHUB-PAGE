
---
title: 'vscode 的 markdown 预览是怎么实现的'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=592'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 06:37:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=592'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>vscode 的 markdown 预览是我们整天都在用的功能，有没有想过它是怎么实现的。或许有一天你会接到个定制 markdown 预览的需求，应该怎么做呢？</p>
<p>其实整体思路比较简单，就是创建一个 webview panel，设置内容为 markdown 生成的 html，之后在 markdown 更新的时候同步修改 webview 的 html 就可以了。</p>
<h2 data-id="heading-0">思路分析</h2>
<p>通过 vscode.window.createWebviewPanel 创建一个 webview，指定在侧边打开，之后通过该  panel 对象的 webview.html 属性来设置 html。</p>
<p>html 是通过编辑器的 markdown 内容生成的， 编辑器内容通过 editor.document.getText() 拿到，然后调用第三方的 markdown 转 html 的库来生成。</p>
<p>这样就完成了 markdown 的预览。</p>
<p>预览之后需要更新，监听 vscode.workspace.onDidSaveTextDocument 和 vscode.workspace.onDidChangeTextDocument 的事件，在文档更新和保存的时候，拿到编辑器的内容，重新生成 html，然后设置到 webview。</p>
<p>webviewPanel 支持 webview.postMessage(message); 的方式传递消息，支持 updateHTML 等一系列 command，可以通过传递消息来触发。</p>
<p>但是怎么知道哪个文档更新哪个 webview 呢？</p>
<p>可以维护一个 map，在创建 webviewPanel 的时候记录到 map 中，key 为文件路径，这样更新的时候就能查找到对应的 webview 进行更新。</p>
<p>这样，就完成了 markdown 内容的更新。</p>
<p>其实整体思路还是比较简单的，下面我们来写下代码</p>
<h2 data-id="heading-1">代码实现</h2>
<p>我们看下 vscode-markdown-preview-enhanced 的插件的代码，这也是一个预览 markdown 的插件，代码还算简洁，可以用来学习。</p>
<p>（以下代码是简化后的代码）</p>
<p>首先，插件要指定触发的条件，也就是在 package.json 里面指定 activationEvents：</p>
<pre><code class="copyable">"activationEvents": [
    "onLanguage:markdown",
    "onCommand:markdown-preview-enhanced.openPreviewToTheSide"
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里一个是编辑 markdown 内容的时候激活，一个是执行 command 的时候激活。</p>
<p>具体激活的逻辑在 active 方法里：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context: vscode.ExtensionContext</span>) </span>&#123;

  <span class="hljs-keyword">const</span> contentProvider = <span class="hljs-keyword">new</span> MarkdownPreviewEnhancedView(context);

  context.subscriptions.push(
    vscode.commands.registerCommand(
      <span class="hljs-string">"markdown-preview-enhanced.openPreviewToTheSide"</span>,
      openPreviewToTheSide,
    ),
  );
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">openPreviewToTheSide</span>(<span class="hljs-params">uri?: vscode.Uri</span>) </span>&#123;
    <span class="hljs-keyword">let</span> resource = uri;
    <span class="hljs-keyword">if</span> (!(resource <span class="hljs-keyword">instanceof</span> vscode.Uri)) &#123;
      <span class="hljs-keyword">if</span> (vscode.window.activeTextEditor) &#123;
        resource = vscode.window.activeTextEditor.document.uri;
      &#125;
    &#125;
    contentProvider.initPreview(resource, vscode.window.activeTextEditor, &#123;
      <span class="hljs-attr">viewColumn</span>: vscode.ViewColumn.Two,
      <span class="hljs-attr">preserveFocus</span>: <span class="hljs-literal">true</span>,
    &#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们注册了那个 command，执行 command 会拿到当前 editor 的 url，然后进行 markdown 的 preview。</p>
<p>preview 的所有逻辑都集中定义在了 MarkdownPreviewEnhancedView 的实例对象中，在 command 触发时执行 initPreivew。</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">public</span> <span class="hljs-keyword">async</span> <span class="hljs-function"><span class="hljs-title">initPreview</span>(<span class="hljs-params">
    sourceUri: vscode.Uri,
    editor: vscode.TextEditor,
    viewOptions: &#123; viewColumn: vscode.ViewColumn; preserveFocus?: <span class="hljs-built_in">boolean</span> &#125;,
</span>)</span> &#123;
    <span class="hljs-comment">// 创建 webview</span>
    <span class="hljs-keyword">let</span> previewPanel: vscode.WebviewPanel = vscode.window.createWebviewPanel(
        <span class="hljs-string">"markdown-preview-enhanced"</span>,
        <span class="hljs-string">`Preview <span class="hljs-subst">$&#123;path.basename(sourceUri.fsPath)&#125;</span>`</span>,
        viewOptions
    );

    <span class="hljs-comment">// 监听 webview 的消息</span>
    previewPanel.webview.onDidReceiveMessage(<span class="hljs-function">(<span class="hljs-params">message</span>) =></span> &#123;&#125;);

    <span class="hljs-comment">// 记录 webview 到 map 中</span>
    <span class="hljs-built_in">this</span>.previewMaps[sourceUri.fsPath] = previewPanel;
    
    <span class="hljs-comment">// 拿到编辑器的文本，生成 html</span>
    <span class="hljs-keyword">const</span> text = editor.document.getText();
    engine
      .generateHTMLTemplateForPreview(&#123;<span class="hljs-attr">inputString</span>: text&#125;)
      .then(<span class="hljs-function">(<span class="hljs-params">html</span>) =></span> &#123;
        <span class="hljs-comment">// 设置 html 到 previewPanel</span>
        previewPanel.webview.html = html;
      &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 initWebivew 里面创建 webviewPanel，同时把 webviewPanel 保存到 map 中，key 为文档的文件路径。拿到编辑器文本来生成 html，设置到 webview.html，这样就完成了 markdown 的预览。</p>
<p>这条路径走通之后，我们就实现了 markdown 的预览。</p>
<p>但是只预览一次不行，更新文档之后需要自动更新，我们继续在 active 方法里添加事件监听：</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  context.subscriptions.push(
    vscode.workspace.onDidSaveTextDocument(<span class="hljs-function">(<span class="hljs-params"><span class="hljs-built_in">document</span></span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (isMarkdownFile(<span class="hljs-built_in">document</span>)) &#123;
        contentProvider.updateMarkdown(<span class="hljs-built_in">document</span>.uri, <span class="hljs-literal">true</span>);
      &#125;
    &#125;),
  );

  context.subscriptions.push(
    vscode.workspace.onDidChangeTextDocument(<span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (isMarkdownFile(event.document)) &#123;
        contentProvider.update(event.document.uri);
      &#125;
    &#125;),
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>监听文本修改和保存的时候，调用 update 方法来更新。</p>
<pre><code class="copyable">public updateMarkdown(sourceUri: Uri) &#123;

    // 从 map 中根据文件路径取出对应的 webviewPanel
    const previewPanel = this.previewMaps[sourceUri.fsPath];
    
    // 生成最新的 html 传递给 webview
    const text = document.getText();
    engine
        .parseMD(text)
        .then((&#123; markdown, html &#125;) => &#123;
            previewPanel.webview.postMessage(&#123;
              command: "updateHTML",
              html
            &#125;);
        &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里是通过 webview.postMessage 给 html 内容传递 updateHTML 的 command 消息，触发 html 内容的更新。</p>
<p>这样，我们就实现了 markdown 的同步刷新。</p>
<h2 data-id="heading-2">总结</h2>
<p>vscode 里面 markdown 的预览是一个常用但实现起来并不难的功能，我们看了下 vscode-markdown-preview-enhanced 插件的源码，理清了整体的流程：</p>
<ul>
<li>通过 vscode.window.createWebviewPanel 创建 webviewPanel 来显示 html</li>
<li>html 通过 editor.document.getText() 拿到文本内容之后通过第三方包生成，设置到 webviewPanel</li>
<li>监听 workspace.onDidSaveTextDocument 和 workspace.onDidChangeTextDocument，来拿到最新内容，之后生成 html 通过 webview.postMessage 传递 udpateHTML 的消息来更新到 webview。</li>
<li>要注意的是，需要记录一个 map 来保存 uri.fsPath 和 webviewPanel 的对应关系，实现文本内容改变更新对应的 webview</li>
</ul>
<p>markdown 的预览是一个常见但是并不难的需求，也比较适合入门 vscode 插件的开发，希望这篇文章能够帮大家理清思路。</p></div>  
</div>
            