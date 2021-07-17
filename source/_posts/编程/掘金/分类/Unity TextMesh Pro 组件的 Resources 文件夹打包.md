
---
title: 'Unity TextMesh Pro 组件的 Resources 文件夹打包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a46597490664ff38fae53d9d528f87c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 03:00:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a46597490664ff38fae53d9d528f87c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">原因</h2>
<p>在使用 Unity 开发的游戏中，避免使用 <strong>Resources</strong> 文件夹，而使用 AssetBundle 打包，但是 TextMesh Pro 组件自带了 <strong>Resources</strong> 文件夹，此时 AssetBundle 资源如果引用了它，那么就会把 TextMesh Pro 打成 AssetBundle，造成冗余。但是如果仅把 TextMesh Pro 的 <strong>Resources</strong> 文件夹改名掉，就会造成【TMP_Settings】读取失败，字体完全无法显示。</p>
<h2 data-id="heading-1">分析</h2>
<p>【TMP_Settings】类是个单例，在初始使用的时候，会去 Resources 文件夹读取资源配置，反射看代码如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">    <span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> TMP_Settings instance
    &#123;
      <span class="hljs-keyword">get</span>
      &#123;
        <span class="hljs-keyword">if</span> ((UnityEngine.Object) TMP_Settings.s_Instance == (UnityEngine.Object) <span class="hljs-literal">null</span>)
          TMP_Settings.s_Instance = UnityEngine.Resources.Load<TMP_Settings>(<span class="hljs-string">"TMP Settings"</span>);
        <span class="hljs-keyword">return</span> TMP_Settings.s_Instance;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也没有接口可以用来赋值<code>TMP_Settings.s_Instance</code>，所以造成后面读取默认字体等失败。</p>
<h2 data-id="heading-2">解决</h2>
<p>既然没有接口可以直接赋值，那么就损失点性能使用反射来对其进行赋值，因为只需赋值一次，所以性能可以忽略。将 Resources 文件夹改名成其他名称，然后把<code>TMP_Settings.asset</code>文件移到 AssetBundle 预制读取目录。最后在游戏资源检测完毕后，调用如下代码：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">    <span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">TMPHelper</span>
    &#123;
        <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">LoadSettings</span>(<span class="hljs-params"></span>)</span>
        &#123;
            TMP_Settings settings = ResManager.LoadAsset<TMP_Settings>(<span class="hljs-string">"Prefab/Configs/TMPPro/TMP_Settings.asset"</span>);
            <span class="hljs-keyword">var</span> settingsType = settings.GetType();
            <span class="hljs-keyword">var</span> settingsInstanceInfo = settingsType.GetField(<span class="hljs-string">"s_Instance"</span>, BindingFlags.Static | BindingFlags.NonPublic);
            settingsInstanceInfo.SetValue(<span class="hljs-literal">null</span>, settings);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样子游戏运行起来就会自动赋值<code>TMP_Settings.s_Instance</code>，但是在编辑器下就无法使用 TextMesh Pro 组件，所以也需要在编辑器下对其进行赋值，添加编辑器类，代码如下：</p>
<pre><code class="hljs language-csharp copyable" lang="csharp">[<span class="hljs-meta">InitializeOnLoad</span>]
<span class="hljs-keyword">public</span> <span class="hljs-keyword">class</span> <span class="hljs-title">GameLauncher</span>
&#123;
    <span class="hljs-function"><span class="hljs-keyword">static</span> <span class="hljs-title">GameLauncher</span>(<span class="hljs-params"></span>)</span>
    &#123;
        LoadSettings();
    &#125;

    <span class="hljs-function"><span class="hljs-keyword">public</span> <span class="hljs-keyword">static</span> <span class="hljs-keyword">void</span> <span class="hljs-title">LoadSettings</span>(<span class="hljs-params"></span>)</span>
    &#123;
        TMP_Settings settings = ResManagerEditor.LoadAssetEditor<TMP_Settings>(<span class="hljs-string">"Prefab/Configs/TMPPro/TMP_Settings.asset"</span>);
        <span class="hljs-keyword">var</span> settingsType = settings.GetType();
        <span class="hljs-keyword">var</span> settingsInstanceInfo = settingsType.GetField(<span class="hljs-string">"s_Instance"</span>, BindingFlags.Static | BindingFlags.NonPublic);
        settingsInstanceInfo.SetValue(<span class="hljs-literal">null</span>, settings);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，只要编辑器一打开就会自动调用赋值。</p>
<h2 data-id="heading-3">其他问题</h2>
<p>更改了 <strong>Resources</strong> 文件夹，会导致文本解析标签失败，即无法内嵌子字体，无法使用如下语法：</p>
<pre><code class="hljs language-xml copyable" lang="xml">Would you like <font="Impact SDF">a different font?<span class="hljs-tag"></<span class="hljs-name">font</span>></span> or just <font="NotoSans" material="NotoSans Outline">a different material?
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a46597490664ff38fae53d9d528f87c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer">
因为内部解析的时候，会去 <strong>Resources</strong> 文件夹下的 <strong>Fonts & Materials</strong> 文件夹寻找字体，寻找不到所以就显示失败。综合考虑不使用这种写法。</p></div>  
</div>
            