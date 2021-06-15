
---
title: 'VS Code插件开发教程（7） Tree View'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07b6b531537a4b2eb757742347cad1eb~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 01:08:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07b6b531537a4b2eb757742347cad1eb~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><code>Tree View API</code>允许插件在<code>sidebar</code>中渲染内容，这些内容以树的形状来展示</p>
<h2 data-id="heading-0">Tree View API基础</h2>
<p>我们通过一个示例来介绍<code>Tree View API</code>相关用法，这个示例利用树视图来展示当前文件夹中所有的<code>Node.js</code>依赖。你可以在 <a href="https://github.com/microsoft/vscode-extension-samples/blob/main/tree-view-sample/README.md" target="_blank" rel="nofollow noopener noreferrer">tree-view-sample</a> 查阅此示例的完整代码</p>
<h3 data-id="heading-1">配置package.json</h3>
<p>首先你要通过 <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.views" target="_blank" rel="nofollow noopener noreferrer">contributes.views</a> 让<code>VS Code</code>知道你要“贡献出”一个视图，下面是<code>package.json</code>的一个初步配置：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"name"</span>: <span class="hljs-string">"helloworld"</span>,
    <span class="hljs-attr">"displayName"</span>: <span class="hljs-string">"HelloWorld"</span>,
    <span class="hljs-attr">"description"</span>: <span class="hljs-string">""</span>,
    <span class="hljs-attr">"version"</span>: <span class="hljs-string">"0.0.1"</span>,
    <span class="hljs-attr">"engines"</span>: &#123;
        <span class="hljs-attr">"vscode"</span>: <span class="hljs-string">"^1.56.0"</span>
    &#125;,
    <span class="hljs-attr">"categories"</span>: [
        <span class="hljs-string">"Other"</span>
    ],
    <span class="hljs-attr">"activationEvents"</span>: [<span class="hljs-string">"onView:nodeDependencies"</span>],
    <span class="hljs-attr">"main"</span>: <span class="hljs-string">"./extension.js"</span>,
    <span class="hljs-attr">"contributes"</span>: &#123;
        <span class="hljs-attr">"views"</span>: &#123;
            <span class="hljs-attr">"explorer"</span>: [&#123;
                <span class="hljs-attr">"id"</span>: <span class="hljs-string">"nodeDependencies"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Node Dependencies"</span>
            &#125;]
        &#125;
    &#125;,
    <span class="hljs-attr">"scripts"</span>: &#123;
        <span class="hljs-attr">"lint"</span>: <span class="hljs-string">"eslint ."</span>,
        <span class="hljs-attr">"pretest"</span>: <span class="hljs-string">"npm run lint"</span>,
        <span class="hljs-attr">"test"</span>: <span class="hljs-string">"node ./test/runTest.js"</span>
    &#125;,
    <span class="hljs-attr">"devDependencies"</span>: &#123;
        <span class="hljs-attr">"@types/vscode"</span>: <span class="hljs-string">"^1.56.0"</span>,
        <span class="hljs-attr">"@types/glob"</span>: <span class="hljs-string">"^7.1.3"</span>,
        <span class="hljs-attr">"@types/mocha"</span>: <span class="hljs-string">"^8.0.4"</span>,
        <span class="hljs-attr">"@types/node"</span>: <span class="hljs-string">"14.x"</span>,
        <span class="hljs-attr">"eslint"</span>: <span class="hljs-string">"^7.19.0"</span>,
        <span class="hljs-attr">"glob"</span>: <span class="hljs-string">"^7.1.6"</span>,
        <span class="hljs-attr">"mocha"</span>: <span class="hljs-string">"^8.2.1"</span>,
        <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.1.3"</span>,
        <span class="hljs-attr">"vscode-test"</span>: <span class="hljs-string">"^1.5.0"</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>仅当用户需要时再去激活插件是十分重要的，例如在本文的示例中，我们可以让插件在用户使用插件视图的时候再去激活。<code>VS Code</code>提供了 <a href="https://code.visualstudio.com/api/references/activation-events#onView" target="_blank" rel="nofollow noopener noreferrer">onView:$&#123;viewId&#125;</a> 事件来告知程序当前用户打开的视图，我们可以在<code>package.json</code>注册一个激活事件<code>"activationEvents": ["onView:nodeDependencies"]</code></p>
<h3 data-id="heading-2">生成数据</h3>
<p>第二步是利用 <a href="https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider" target="_blank" rel="nofollow noopener noreferrer">TreeDataProvider</a> 生成树视图所需的<code>Node.js</code>依赖的数据，其中需要实现两个方法：</p>
<ul>
<li><code>getChildren(element?: T): ProviderResult<T[]></code>：返回指定节点（如果没有指定就是根节点）的子节点</li>
<li><code>getTreeItem(element: T): TreeItem | Thenable<TreeItem></code>：返回用于在视图里展示的UI节点</li>
</ul>
<p>每当用户打开树视图，<code>getChildren</code>会被自动调用（没有参数），你可以在这里返回树视图的第一层级内容。在示例中，我们用<code>TreeItemCollapsibleState.Collapsed</code>（折叠）、<code>TreeItemCollapsibleState.Expanded</code>（展开）、<code>TreeItemCollapsibleState.None</code>（无子节点，不会触发<code>getChildren</code>方法）控制节点的折叠状态，下面是一个<code>TreeDataProvider</code>的实现示例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> vscode <span class="hljs-keyword">from</span> <span class="hljs-string">'vscode'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NodeDependenciesProvider</span> <span class="hljs-title">implements</span> <span class="hljs-title">vscode</span>.<span class="hljs-title">TreeDataProvider</span><<span class="hljs-title">Dependency</span>> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">private workspaceRoot: string</span>)</span> &#123; &#125;

    getTreeItem(element: Dependency): vscode.TreeItem &#123;
        <span class="hljs-keyword">return</span> element;
    &#125;

    getChildren(element?: Dependency): Thenable<Dependency[]> &#123;
        <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.workspaceRoot) &#123;
            vscode.window.showInformationMessage(<span class="hljs-string">'No dependency in empty workspace'</span>);
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve([]);
        &#125;

        <span class="hljs-keyword">if</span> (element) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(
                <span class="hljs-built_in">this</span>.getDepsInPackageJson(
                    path.join(<span class="hljs-built_in">this</span>.workspaceRoot, <span class="hljs-string">'node_modules'</span>, element.label, <span class="hljs-string">'package.json'</span>)
                )
            );
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">const</span> packageJsonPath = path.join(<span class="hljs-built_in">this</span>.workspaceRoot, <span class="hljs-string">'package.json'</span>);
            <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pathExists(packageJsonPath)) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-built_in">this</span>.getDepsInPackageJson(packageJsonPath));
            &#125; <span class="hljs-keyword">else</span> &#123;
                vscode.window.showInformationMessage(<span class="hljs-string">'Workspace has no package.json'</span>);
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve([]);
            &#125;
        &#125;
    &#125;

    <span class="hljs-comment">/**
     * Given the path to package.json, read all its dependencies
     */</span>
    private getDepsInPackageJson(packageJsonPath: string): Dependency[] &#123;
        <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pathExists(packageJsonPath)) &#123;
            <span class="hljs-keyword">const</span> toDep = (moduleName: string, <span class="hljs-attr">version</span>: string): <span class="hljs-function"><span class="hljs-params">Dependency</span> =></span> &#123;
                <span class="hljs-keyword">const</span> depPackageJsonPath = path.join(<span class="hljs-built_in">this</span>.workspaceRoot, <span class="hljs-string">'node_modules'</span>, moduleName, <span class="hljs-string">'package.json'</span>);
                <span class="hljs-keyword">let</span> collapsibleState = vscode.TreeItemCollapsibleState.Collapsed;
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.pathExists(depPackageJsonPath)) &#123;
                    <span class="hljs-keyword">const</span> depPackageJson = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(depPackageJsonPath, <span class="hljs-string">'utf-8'</span>));
                    <span class="hljs-comment">// 如果依赖的代码包已经安装（node_modules有内容），且这个安装包本身有dependencies或devDependencies，才设置为可展开的</span>
                    <span class="hljs-keyword">if</span> ((!depPackageJson.dependencies || <span class="hljs-built_in">Object</span>.keys(depPackageJson.dependencies).length === <span class="hljs-number">0</span>) &&
                        (!depPackageJson.devDependencies || <span class="hljs-built_in">Object</span>.keys(depPackageJson.devDependencies).length === <span class="hljs-number">0</span>)) &#123;
                        collapsibleState = vscode.TreeItemCollapsibleState.None;
                    &#125;
                &#125;
                <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Dependency(moduleName, version, collapsibleState);
            &#125;;
            <span class="hljs-keyword">const</span> packageJson = <span class="hljs-built_in">JSON</span>.parse(fs.readFileSync(packageJsonPath, <span class="hljs-string">'utf-8'</span>));
            <span class="hljs-keyword">const</span> deps = packageJson.dependencies
                ? <span class="hljs-built_in">Object</span>.keys(packageJson.dependencies).map(<span class="hljs-function"><span class="hljs-params">dep</span> =></span>
                    toDep(dep, packageJson.dependencies[dep])
                )
                : [];
            <span class="hljs-keyword">const</span> devDeps = packageJson.devDependencies
                ? <span class="hljs-built_in">Object</span>.keys(packageJson.devDependencies).map(<span class="hljs-function"><span class="hljs-params">dep</span> =></span>
                    toDep(dep, packageJson.devDependencies[dep])
                )
                : [];
            <span class="hljs-keyword">return</span> deps.concat(devDeps);
        &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-keyword">return</span> [];
        &#125;
    &#125;

    private pathExists(p: string): boolean &#123;
        <span class="hljs-keyword">try</span> &#123;
            fs.accessSync(p);
        &#125; <span class="hljs-keyword">catch</span> (err) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
    &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dependency</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">vscode</span>.<span class="hljs-title">TreeItem</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">
        public readonly label: string,
        private version: string,
        public readonly collapsibleState: vscode.TreeItemCollapsibleState
    </span>)</span> &#123;
        <span class="hljs-built_in">super</span>(label, collapsibleState);
        <span class="hljs-built_in">this</span>.tooltip = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.label&#125;</span>-<span class="hljs-subst">$&#123;<span class="hljs-built_in">this</span>.version&#125;</span>`</span>;
        <span class="hljs-built_in">this</span>.description = <span class="hljs-built_in">this</span>.version;
    &#125;

    iconPath = &#123;
        <span class="hljs-attr">light</span>: path.join(__filename, <span class="hljs-string">'..'</span>, <span class="hljs-string">'..'</span>, <span class="hljs-string">'resources'</span>, <span class="hljs-string">'light'</span>, <span class="hljs-string">'dependency.svg'</span>),
        <span class="hljs-attr">dark</span>: path.join(__filename, <span class="hljs-string">'..'</span>, <span class="hljs-string">'..'</span>, <span class="hljs-string">'resources'</span>, <span class="hljs-string">'dark'</span>, <span class="hljs-string">'dependency.svg'</span>)
    &#125;;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">注册TreeDataProvider</h3>
<p>第三步是将生成的依赖数据提供给视图，可以通过两种方式实现：</p>
<ul>
<li>
<p><code>vscode.window.registerTreeDataProvider</code>：注册树数据的<code>provider</code>，需要提供视图ID和数据<code>provider</code>对象</p>
<pre><code class="hljs language-js copyable" lang="js">vscode.window.registerTreeDataProvider(
    <span class="hljs-string">'nodeDependencies'</span>,
    <span class="hljs-keyword">new</span> NodeDependenciesProvider(vscode.workspace.rootPath)
);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>vscode.window.createTreeView</code>：通过视图ID和数据<code>provider</code>来创建视树视图，这会提供访问 <a href="https://code.visualstudio.com/api/references/vscode-api#TreeView" target="_blank" rel="nofollow noopener noreferrer">树视图</a> 的能力，如果你需要使用<code>TreeView API</code>，可以使用<code>createTreeView</code>的方式</p>
<pre><code class="hljs language-js copyable" lang="js">vscode.window.createTreeView(<span class="hljs-string">'nodeDependencies'</span>, &#123;
    <span class="hljs-attr">treeDataProvider</span>: <span class="hljs-keyword">new</span> NodeDependenciesProvider(vscode.workspace.rootPath)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>至此一个具备基本目标功能的插件就已经完成，可以看到实际效果如下：</p>
<img width="100%" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07b6b531537a4b2eb757742347cad1eb~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>上述代码的完整示例参见 <a href="https://github.com/king-king/vscode-extension/tree/tree-view-v1-update1/packages/tree-view-test" target="_blank" rel="nofollow noopener noreferrer">tree-view-test v1</a></p>
<h3 data-id="heading-4">更新视图内容</h3>
<h4 data-id="heading-5">以命令行方式</h4>
<p>目前完成的这个插件仅具备最基本的功能，数依赖数据一经展示便无法更新。如果在视图中有一个刷新按钮将会是非常方便的，为了实现这个目标，我们需要利用 <a href="https://code.visualstudio.com/api/references/vscode-api#TreeDataProvider" target="_blank" rel="nofollow noopener noreferrer">onDidChangeTreeData</a> 事件：</p>
<ul>
<li><code>onDidChangeTreeData?: Event<T | undefined | null | void></code>：当依赖数据变更并且你希望更新树视图的时候执行</li>
</ul>
<p>在<code>provider</code>中添加如下代码：</p>
<pre><code class="hljs language-js copyable" lang="js">    private _onDidChangeTreeData: vscode.EventEmitter<Dependency | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span> | <span class="hljs-keyword">void</span>> = <span class="hljs-keyword">new</span> vscode.EventEmitter<Dependency | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span> | <span class="hljs-keyword">void</span>>();
    readonly onDidChangeTreeData: vscode.Event<Dependency | <span class="hljs-literal">undefined</span> | <span class="hljs-literal">null</span> | <span class="hljs-keyword">void</span>> = <span class="hljs-built_in">this</span>._onDidChangeTreeData.event;
    refresh(): <span class="hljs-keyword">void</span> &#123;
        <span class="hljs-built_in">this</span>._onDidChangeTreeData.fire();
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们有了更新函数，但没有调用它，我们可以在<code>package.json</code>中定义一条更新命令：</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"commands"</span>: [
            &#123;
                <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.refreshEntry"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Refresh Dependence"</span>,
                <span class="hljs-attr">"icon"</span>: &#123;
                    <span class="hljs-attr">"light"</span>: <span class="hljs-string">"resources/light/refresh.svg"</span>,
                    <span class="hljs-attr">"dark"</span>: <span class="hljs-string">"resources/dark/refresh.svg"</span>
                &#125;
            &#125;
    ]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后注册该命令：</p>
<pre><code class="hljs language-js copyable" lang="js">  vscode.commands.registerCommand(<span class="hljs-string">'nodeDependencies.refreshEntry'</span>, <span class="hljs-function">() =></span>
      nodeDependenciesProvider.refresh()
  );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时我们会看到，当执行了<code>Refresh Dependence</code>命令后，<code>Node.js</code>依赖的树视图会被更新：
<img width="100%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e325d3c95f54426ab0047b0a0550d42e~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">以按钮方式</h4>
<p>在前文的基础上，如果在视图中添加一个按钮或许操作的时候有会更加直观、友好。我们在<code>package.json</code>中添加：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"menus"</span>: &#123;
    <span class="hljs-attr">"view/title"</span>: [
        &#123;
            <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.refreshEntry"</span>,
            <span class="hljs-attr">"when"</span>: <span class="hljs-string">"view == nodeDependencies"</span>,
            <span class="hljs-attr">"group"</span>: <span class="hljs-string">"navigation"</span>
        &#125;,
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时当我们将鼠标浮在视图上时就会看到刷新按钮，点击效果同执行<code>Refresh Dependence</code>命令：</p>
<img width="60%" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25b993769a0c4f87a2844613ff0127e8~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p><code>group</code>属性用于菜单项的排序和分类，其中值为<code>navigation</code>的<code>group</code>是用来将置顶的，如果不设置，则刷新按钮将会被隐藏在“...”里，效果如下所示：</p>
<img width="60%" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62abf28fe15c4a9cb5a2b2f76a28ee3a~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>上述代码的完整示例参见 <a href="https://github.com/king-king/vscode-extension/tree/tree-view-v2/packages/tree-view-test" target="_blank" rel="nofollow noopener noreferrer">tree-view-test v2</a></p>
<h2 data-id="heading-7">添加到视图容器（View Container）</h2>
<h3 data-id="heading-8">创建视图容器</h3>
<p>视图容器包含了一系列展示在<code>Activity Bar</code>或<code>Panel</code>中的视图，如果希望自己的插件自定义一个视图容器，我们可以用 <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.viewsContainers" target="_blank" rel="nofollow noopener noreferrer">contributes.viewsContainers </a> 在<code>package.json</code>中注册：</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"contributes"</span>: &#123;
        <span class="hljs-attr">"viewsContainers"</span>: &#123;
            <span class="hljs-attr">"activitybar"</span>: [&#123;
                <span class="hljs-attr">"id"</span>: <span class="hljs-string">"package-explorer"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Package Explorer"</span>,
                <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"media/dep.svg"</span>
            &#125;]
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者你也可以在<code>panel</code>字段下做配置</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"contributes"</span>: &#123;
        <span class="hljs-attr">"viewsContainers"</span>: &#123;
           <span class="hljs-attr">"panel"</span>: [&#123;
                <span class="hljs-attr">"id"</span>: <span class="hljs-string">"package-explorer"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Package Explorer"</span>,
                <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"media/dep.svg"</span>
            &#125;]
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">将视图和视图容器绑定</h3>
<p>我们可以在<code>package.json</code>中用 <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.views" target="_blank" rel="nofollow noopener noreferrer">contributes.views</a> 来实现</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"contributes"</span>: &#123;
        <span class="hljs-attr">"views"</span>: &#123;
            <span class="hljs-attr">"package-explorer"</span>: [&#123;
                <span class="hljs-attr">"id"</span>: <span class="hljs-string">"nodeDependencies"</span>,
                <span class="hljs-attr">"name"</span>: <span class="hljs-string">"Node Dependencies"</span>,
                <span class="hljs-attr">"icon"</span>: <span class="hljs-string">"media/dep.svg"</span>,
                <span class="hljs-attr">"contextualTitle"</span>: <span class="hljs-string">"Package Explorer"</span>
            &#125;]
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要注意的是，一个视图可以设置<code>visibility</code>属性，该属性有三个取值：<code>visible</code>、<code>collapsed</code>、<code>hidden</code>，这三个值仅在首次打开工作台的时候起作用，之后其取值取决于用户的控制。如果你的视图容器里有很多的视图，则可以利用该属性让你的界面更加简洁</p>
<img width="50%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6da75167414c48a9b3cdec7106fdb540~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<img width="50%" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9c9309672724e4b8568cc9de6c88273~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>现在我们可以看到左侧的视图容器和树视图了：</p>
<img width="50%" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0d010ee06184051a7385bb42845b104~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>上述代码的完整示例参见 <a href="https://github.com/king-king/vscode-extension/tree/tree-view-v3/packages/tree-view-test" target="_blank" rel="nofollow noopener noreferrer">tree-view-test v3</a></p>
<h2 data-id="heading-10">视图行为解读</h2>
<p>视图的行为附着在视图的内联图标上，这些图标可以在树视图中的每一个节点上、还可以在树视图顶端的标题栏上，我们可以在<code>package.json</code>中对其进行配置：</p>
<ul>
<li><code>view/title</code>：位置在视图标题栏上，可以用<code>"group": "navigation"</code>来保证其优先级</li>
<li><code>view/item/context</code>：位置在树节点上，可以用<code>"group": "inline"</code>让其内联显示</li>
</ul>
<blockquote>
<p>上述均可用 <a href="https://code.visualstudio.com/api/references/when-clause-contexts" target="_blank" rel="nofollow noopener noreferrer">when clause</a> 控制其生效条件</p>
</blockquote>
<img width="100%" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0436ad24f874f9c991b02f7e38cc939~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>如果我们想实现上图的效果，可以用如下代码实现：</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"contributes"</span>: &#123;
        <span class="hljs-attr">"commands"</span>: [&#123;
                <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.refreshEntry"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Refresh"</span>,
                <span class="hljs-attr">"icon"</span>: &#123;
                    <span class="hljs-attr">"light"</span>: <span class="hljs-string">"resources/light/refresh.svg"</span>,
                    <span class="hljs-attr">"dark"</span>: <span class="hljs-string">"resources/dark/refresh.svg"</span>
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.addEntry"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Add"</span>
            &#125;,
            &#123;
                <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.editEntry"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Edit"</span>,
                <span class="hljs-attr">"icon"</span>: &#123;
                    <span class="hljs-attr">"light"</span>: <span class="hljs-string">"resources/light/edit.svg"</span>,
                    <span class="hljs-attr">"dark"</span>: <span class="hljs-string">"resources/dark/edit.svg"</span>
                &#125;
            &#125;,
            &#123;
                <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.deleteEntry"</span>,
                <span class="hljs-attr">"title"</span>: <span class="hljs-string">"Delete"</span>
            &#125;
        ],
        <span class="hljs-attr">"menus"</span>: &#123;
            <span class="hljs-attr">"view/title"</span>: [&#123;
                    <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.refreshEntry"</span>,
                    <span class="hljs-attr">"when"</span>: <span class="hljs-string">"view == nodeDependencies"</span>,
                    <span class="hljs-attr">"group"</span>: <span class="hljs-string">"navigation"</span>
                &#125;,
                &#123;
                    <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.addEntry"</span>,
                    <span class="hljs-attr">"when"</span>: <span class="hljs-string">"view == nodeDependencies"</span>
                &#125;
            ],
            <span class="hljs-attr">"view/item/context"</span>: [&#123;
                    <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.editEntry"</span>,
                    <span class="hljs-attr">"when"</span>: <span class="hljs-string">"view == nodeDependencies && viewItem == dependency"</span>,
                    <span class="hljs-attr">"group"</span>: <span class="hljs-string">"inline"</span>
                &#125;,
                &#123;
                    <span class="hljs-attr">"command"</span>: <span class="hljs-string">"nodeDependencies.deleteEntry"</span>,
                    <span class="hljs-attr">"when"</span>: <span class="hljs-string">"view == nodeDependencies && viewItem == dependency"</span>
                &#125;
            ]
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们可以在<code>when</code>字段中使用 <a href="https://code.visualstudio.com/api/references/vscode-api#TreeItem" target="_blank" rel="nofollow noopener noreferrer">TreeItem.contextValue</a> 的数据，来控制相应行为的显示</p>
</blockquote>
<p>上述代码的完整示例参见 <a href="https://github.com/king-king/vscode-extension/tree/tree-view-v4/packages/tree-view-test" target="_blank" rel="nofollow noopener noreferrer">tree-view-test v4</a></p>
<h2 data-id="heading-11">视图欢迎内容</h2>
<p>我们可以添加一个欢迎内容，以便当视图内容初始化或为空的时候显示：</p>
<pre><code class="hljs language-json copyable" lang="json">    <span class="hljs-string">"contributes"</span>: &#123;
        <span class="hljs-attr">"viewsWelcome"</span>: [&#123;
            <span class="hljs-attr">"view"</span>: <span class="hljs-string">"nodeDependencies"</span>,
            <span class="hljs-attr">"contents"</span>: <span class="hljs-string">"没有发现依赖内容， [了解更多](https://www.npmjs.com/).\n[添加依赖](command:nodeDependencies.addEntry)"</span>
        &#125;]
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>contributes.viewsWelcome.contents</code>支持链接，如果链接单起一行，会被渲染为按钮。每个<code>viewsWelcome</code>支持 <a href="https://code.visualstudio.com/api/references/when-clause-contexts" target="_blank" rel="nofollow noopener noreferrer">when clause</a></p>
<img width="100%" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb62b497c6df4ef7b55acdff1614a3f0~tplv-k3u1fbpfcp-watermark.image" loading="lazy" referrerpolicy="no-referrer">
<p>上述代码的完整示例参见 <a href="https://github.com/king-king/vscode-extension/tree/tree-view-v5/packages/tree-view-test" target="_blank" rel="nofollow noopener noreferrer">tree-view-test v5</a></p></div>  
</div>
            