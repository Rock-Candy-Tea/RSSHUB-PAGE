
---
title: 'Node脚本快速同步CNPM项目内用到的依赖'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c07be700f41149928c26b6ce7e59648d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 01 May 2021 10:18:11 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c07be700f41149928c26b6ce7e59648d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>还是为了解决之前的问题;<br>公司用CNPM作为内部私有仓,没有开启全量实时同步;<br>所以有些包会相对落后,所以常用同步上游就显得很重要了;<br>
<br>我想了想,每次都要手动去执行个别的包或者少量包的查询,操作太多了;<br>原理还是遵循CNPM更新机制,可以看看上篇帖子哈~<br></p>
<h2 data-id="heading-1">考虑的点</h2>
<ul>
<li>设置一个根路径,会自动检索下所有项目的packaeg.json(不包含node_modules)
<ul>
<li>包括所有git subtree或者monorepo的package.json</li>
</ul>
</li>
<li>支持延时执行,一瞬间太多要同步的,会把内部搭建cnpm搞崩;</li>
<li>同步过,再下一个执行同步的会自动过滤.也就是同步过同名包不会再发同步请求</li>
</ul>
<p><br>使用成本极低,一个Node环境装几个常用的npm包;
<a name="user-content-De7bL" href="https://juejin.cn/post/undefined"></a></p>
<h2 data-id="heading-2">环境</h2>
<ul>
<li>Node 14.16.1</li>
</ul>
<h2 data-id="heading-3">效果图</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c07be700f41149928c26b6ce7e59648d~tplv-k3u1fbpfcp-zoom-1.image" alt="2021-05-02 02.09.35.gif" loading="lazy" referrerpolicy="no-referrer"><br></p>
<h2 data-id="heading-4">源码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> globby = <span class="hljs-built_in">require</span>(<span class="hljs-string">'globby'</span>);
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>);
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>);
<span class="hljs-keyword">const</span> axios = <span class="hljs-built_in">require</span>(<span class="hljs-string">'axios'</span>);
<span class="hljs-keyword">const</span> chalk = <span class="hljs-built_in">require</span>(<span class="hljs-string">'chalk'</span>);
<span class="hljs-keyword">const</span> isPlainObject = <span class="hljs-built_in">require</span>(<span class="hljs-string">'lodash/isPlainObject'</span>);
<span class="hljs-keyword">const</span> options = &#123;
    <span class="hljs-attr">baseRootPath</span>: <span class="hljs-string">'/Users/linqunhe/Code'</span>,  <span class="hljs-comment">// 检索的根路径</span>
    <span class="hljs-attr">ignorePackage</span>: [<span class="hljs-string">'@ones-ai'</span>, <span class="hljs-string">'@ones'</span>], <span class="hljs-comment">// 忽略的包名,就是不管有木有缓存都不同步</span>
    <span class="hljs-attr">delayTime</span>: <span class="hljs-number">2000</span>, <span class="hljs-comment">// 每一次执行延时的时间,随着执行次数会递增 , 2000 = 2s</span>
    <span class="hljs-attr">maxRetry</span>: <span class="hljs-number">3</span>, <span class="hljs-comment">// 整个逻辑,中间有错误重试机制最大次数</span>
&#125;
<span class="hljs-keyword">let</span> cachePkgList = [];
<span class="hljs-keyword">let</span> retryCount = <span class="hljs-number">0</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onesNpmSyncUpdate</span>(<span class="hljs-params">pkgList, isArray = <span class="hljs-literal">false</span></span>) </span>&#123;
    <span class="hljs-keyword">const</span> pkg = isArray ? pkgList.join(<span class="hljs-string">','</span>) : pkgList
    <span class="hljs-keyword">return</span> axios.put(<span class="hljs-string">`https://npm.myones.net/sync/<span class="hljs-subst">$&#123;pkg&#125;</span>?sync_upstream=true`</span>).then(<span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (res && res.data && res.data.ok) &#123;
            <span class="hljs-keyword">const</span> data = [
                &#123;
                    <span class="hljs-string">'执行时间'</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().toISOString(),
                    <span class="hljs-string">'NPM包名'</span>: isArray ? <span class="hljs-built_in">JSON</span>.stringify(pkgList) : pkgList,
                    <span class="hljs-string">'同步状态'</span>: res.data.ok
                &#125;
            ]
            <span class="hljs-built_in">console</span>.dir(data);
        &#125;
    &#125;).catch(<span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'🍑 NPM包名'</span>, chalk.red(<span class="hljs-string">`<span class="hljs-subst">$&#123;pkg&#125;</span>`</span>.padEnd(<span class="hljs-number">60</span>)), <span class="hljs-string">'👀 同步状态:  '</span>, chalk.green(<span class="hljs-string">'false'</span>));
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">arrayTypeData</span>(<span class="hljs-params">array</span>) </span>&#123;
    <span class="hljs-keyword">let</span> decoratorsArr = []
    <span class="hljs-keyword">let</span> normalArr = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> item <span class="hljs-keyword">of</span> array) &#123;
        <span class="hljs-keyword">if</span> (item && <span class="hljs-keyword">typeof</span> item === <span class="hljs-string">'string'</span>) &#123;
            <span class="hljs-keyword">if</span> (item.startsWith(<span class="hljs-string">'@'</span>) && item.includes(<span class="hljs-string">'/'</span>)) &#123;
                decoratorsArr.push(item)
            &#125; <span class="hljs-keyword">else</span> &#123;
                normalArr.push(item)
            &#125;
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> &#123;
        decoratorsArr,
        normalArr
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getPackageJsonDepKey</span>(<span class="hljs-params">json = &#123; dependencies: &#123;&#125;, devDependencies: &#123;&#125; &#125;, ignore = []</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; dependencies, devDependencies, peerDependencies &#125; = json;
    <span class="hljs-keyword">let</span> dependenciesKey = [];
    <span class="hljs-keyword">let</span> devDependenciesKey = [];
    <span class="hljs-keyword">let</span> peerDependenciesKey = [];
    <span class="hljs-keyword">if</span> (dependencies && isPlainObject(dependencies)) &#123;
        dependenciesKey = <span class="hljs-built_in">Object</span>.keys(dependencies);
    &#125;

    <span class="hljs-keyword">if</span> (devDependencies && isPlainObject(devDependencies)) &#123;
        devDependenciesKey = <span class="hljs-built_in">Object</span>.keys(devDependencies);
    &#125;
    <span class="hljs-keyword">if</span> (peerDependencies && isPlainObject(peerDependencies)) &#123;
        peerDependenciesKey = <span class="hljs-built_in">Object</span>.keys(peerDependencies);
    &#125;

    <span class="hljs-keyword">const</span> allDepKey = [...new <span class="hljs-built_in">Set</span>([...dependenciesKey, ...devDependenciesKey, ...peerDependenciesKey])]
    <span class="hljs-keyword">return</span> allDepKey.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">const</span> iterator <span class="hljs-keyword">of</span> ignore) &#123;
            <span class="hljs-keyword">if</span> (item.indexOf(iterator) !== -<span class="hljs-number">1</span>) &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
            &#125;
        &#125;
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">readPackageJson</span>(<span class="hljs-params">path</span>) </span>&#123;
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">const</span> data = fs.readFileSync(path, &#123; <span class="hljs-attr">encoding</span>: <span class="hljs-string">'utf8'</span> &#125;);
        <span class="hljs-keyword">if</span> (data && <span class="hljs-keyword">typeof</span> data === <span class="hljs-string">'string'</span>) &#123;
            <span class="hljs-keyword">return</span> <span class="hljs-built_in">JSON</span>.parse(data)
        &#125;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'%c 🍦 error: '</span>, <span class="hljs-string">'font-size:20px;background-color: #EA7E5C;color:#fff;'</span>, path, error);
    &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getUpdatePkgList</span>(<span class="hljs-params">depKeyArr</span>) </span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(depKeyArr) && depKeyArr.length <=<span class="hljs-number">0</span>) <span class="hljs-keyword">return</span> [];
    <span class="hljs-keyword">let</span> newUpdatePkgList = [];
    <span class="hljs-keyword">let</span> uniDepKeyArr = [...new <span class="hljs-built_in">Set</span>(depKeyArr)];
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(cachePkgList)) &#123;
        <span class="hljs-keyword">if</span> (cachePkgList.length <= <span class="hljs-number">0</span>) &#123;
            cachePkgList = uniDepKeyArr;
            newUpdatePkgList = cachePkgList;
        &#125; <span class="hljs-keyword">else</span> &#123;
            newUpdatePkgList = uniDepKeyArr.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> !cachePkgList.includes(item))
            cachePkgList = [...new <span class="hljs-built_in">Set</span>(cachePkgList.concat(uniDepKeyArr))]
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> newUpdatePkgList
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updatePkgList</span>(<span class="hljs-params">depKeyArr, index</span>) </span>&#123;
    <span class="hljs-keyword">const</span> &#123; decoratorsArr, normalArr &#125; = arrayTypeData(depKeyArr);

    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(normalArr) && normalArr.length > <span class="hljs-number">0</span>) &#123;
        onesNpmSyncUpdate(normalArr, <span class="hljs-literal">true</span>)
    &#125;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(decoratorsArr) && decoratorsArr.length > <span class="hljs-number">0</span>) &#123;
        decoratorsArr.forEach(<span class="hljs-function"><span class="hljs-params">item</span> =></span> &#123;
            onesNpmSyncUpdate(item)
        &#125;)
    &#125;
&#125;

<span class="hljs-keyword">const</span> sleep = <span class="hljs-function">(<span class="hljs-params">time</span>) =></span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve</span>) =></span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🎳🎳🎳 <span class="hljs-subst">$&#123;chalk.green(<span class="hljs-string">`<span class="hljs-subst">$&#123;time / <span class="hljs-number">1000</span>&#125;</span> s`</span>)&#125;</span> 后执行更新操作!`</span>);
    <span class="hljs-built_in">setTimeout</span>(resolve, time);
&#125;)

<span class="hljs-keyword">const</span> getExecFileBaseInfo = <span class="hljs-function">(<span class="hljs-params">abPath</span>) =></span> &#123;
    <span class="hljs-keyword">const</span> &#123; base, dir, ext &#125; = path.parse(abPath);
    <span class="hljs-keyword">const</span> data = [&#123;
        <span class="hljs-string">'执行时间'</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().toISOString(),
        <span class="hljs-string">'所在目录'</span>: dir,
        <span class="hljs-string">'执行文件'</span>: base,
        <span class="hljs-string">'文件类型'</span>: ext,
    &#125;]
    <span class="hljs-built_in">console</span>.table(data);
&#125;

<span class="hljs-keyword">const</span> runScript = <span class="hljs-keyword">async</span> (options) => &#123;
    <span class="hljs-keyword">const</span> pkgGlob = <span class="hljs-string">`<span class="hljs-subst">$&#123;options.baseRootPath&#125;</span>/**/**/package.json`</span>;
    <span class="hljs-keyword">let</span> index = <span class="hljs-number">1</span>;
    <span class="hljs-keyword">let</span> execTime = <span class="hljs-number">1000</span>;
    <span class="hljs-keyword">let</span> depKeyArr = [];
    <span class="hljs-keyword">try</span> &#123;
        <span class="hljs-keyword">for</span> <span class="hljs-keyword">await</span> (<span class="hljs-keyword">const</span> path <span class="hljs-keyword">of</span> globby.stream(pkgGlob, &#123; <span class="hljs-attr">ignore</span>: [<span class="hljs-string">'**/node_modules'</span>] &#125;)) &#123;
            <span class="hljs-keyword">const</span> packageJson = readPackageJson(path);
            <span class="hljs-keyword">if</span> (packageJson && isPlainObject(packageJson)) &#123;
                <span class="hljs-keyword">const</span> packageDepKey = getPackageJsonDepKey(packageJson, options.ignorePackage);
                <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(packageDepKey) && packageDepKey.length > <span class="hljs-number">0</span>) &#123;
                    depKeyArr = [...depKeyArr, ...packageDepKey]
                &#125;
            &#125;
            <span class="hljs-keyword">const</span> newUpdatePkgList = getUpdatePkgList(depKeyArr);
            <span class="hljs-keyword">if</span> (newUpdatePkgList.length <= <span class="hljs-number">0</span>) &#123;
                <span class="hljs-keyword">continue</span>
            &#125; <span class="hljs-keyword">else</span> &#123;
                getExecFileBaseInfo(path);
                <span class="hljs-keyword">if</span> (index <= <span class="hljs-number">1</span>) &#123;
                    updatePkgList(newUpdatePkgList, index);
                &#125; <span class="hljs-keyword">else</span> &#123;
                    <span class="hljs-keyword">await</span> sleep(execTime * index)
                    updatePkgList(newUpdatePkgList, index);

                &#125;
                index = ++index;
            &#125;
        &#125;
    &#125; <span class="hljs-keyword">catch</span> (error) &#123;
        <span class="hljs-keyword">if</span> (error) &#123;
            <span class="hljs-keyword">if</span> (retryCount < options.maxRetry) &#123;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'%c 🍞 error: '</span>, <span class="hljs-string">'font-size:20px;background-color: #B03734;color:#fff;'</span>, error, <span class="hljs-string">'准备重试'</span>);
                runScript(options);
                retryCount = ++retryCount;
            &#125;
        &#125;

    &#125;

&#125;

runScript(options);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">总结</h2>
<p>现在这样就很方便了.随着我本地的项目越来越多.<br>我只要定期更新一次就可以满足挺久的使用;<br>而且也不需要全量同步CNPM这么夸张,<br>只同步使用到的,又能跟进上游!!<br>有不对之处请留言,谢谢阅读!</p></div>  
</div>
            