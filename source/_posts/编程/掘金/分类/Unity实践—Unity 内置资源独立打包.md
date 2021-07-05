
---
title: 'Unity实践—Unity 内置资源独立打包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://dm2305files.storage.live.com/y4mmT4GmOESf-Yj4xXbLEeku6KcZpswW0VChnprWCTy4fv92n0KWoMpTcycYJocT3XvU0C3BH4jiVqz01lKg_bbR44ZaTFS3WuEYCItP2qXjN5F-cRs4jpVVxV4GV05yyqwWji_XJdLdq3T5XUoKTOJFoBvDkR06T4OJ3xqredPuTSBWeKHdqZYx08B-91pNqJr?width=356&height=332&cropmode=none'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 08:48:34 GMT
thumbnail: 'https://dm2305files.storage.live.com/y4mmT4GmOESf-Yj4xXbLEeku6KcZpswW0VChnprWCTy4fv92n0KWoMpTcycYJocT3XvU0C3BH4jiVqz01lKg_bbR44ZaTFS3WuEYCItP2qXjN5F-cRs4jpVVxV4GV05yyqwWji_XJdLdq3T5XUoKTOJFoBvDkR06T4OJ3xqredPuTSBWeKHdqZYx08B-91pNqJr?width=356&height=332&cropmode=none'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>针对内置资源重复打包冗余的问题，编写 Addressables Build 脚本将内置资源独立打包<br>
本人原博：<a href="https://warl-g.github.io/posts/Unity-BuiltIn-Pack/" target="_blank" rel="nofollow noopener noreferrer">Warl-G's Blog - Unity实践—Unity 内置资源独立打包</a></p>
<h2 data-id="heading-0">什么是内置资源</h2>
<p>Unity 提供了一些内置资源，可在编辑器中找到内置资源包<code>unity_builtin_extra</code></p>
<ul>
<li>Windows: <code>~/Editor/Data/Resources/unity_builtin_extra</code></li>
<li>MacOS:<code>~/Unity.app/Contents/Resources/unity_builtin_extra</code></li>
</ul>
<p><code>unity_builtin_extra</code> 中包含了一系列默认 Shader 和贴图等资源，可在编辑器中直接选择</p>
<p><img src="https://dm2305files.storage.live.com/y4mmT4GmOESf-Yj4xXbLEeku6KcZpswW0VChnprWCTy4fv92n0KWoMpTcycYJocT3XvU0C3BH4jiVqz01lKg_bbR44ZaTFS3WuEYCItP2qXjN5F-cRs4jpVVxV4GV05yyqwWji_XJdLdq3T5XUoKTOJFoBvDkR06T4OJ3xqredPuTSBWeKHdqZYx08B-91pNqJr?width=356&height=332&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://dm2305files.storage.live.com/y4mulECCyBOMqZKTaMg97CwDbjw3XScDvbjHG40tWsBjmeppaL_gi9cvQGbhngUdVMUAVN5yUYaaON2HYzv7-ksm7JvEs01lo_vP2AQi5AzW14TfErvT0MA1A6tnKETA2OSUu3gDUZAR38ygv-A3QybREveeD9KyjirO2ERbnXbiPubVNoZt6hSWdk5tAXMNSQz?width=360&height=603&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>由上图可见内置贴图资源路径为 <code>Resources/unity_builtin_extra</code>，在代码中可使用<code>AssetDatabase.GetAssetPath</code> 得到同样的路径</p>
<p>但无法通过该路径读取资源，编辑器下可用接口<code>AssetDatabase.GetBuiltinExtraResource</code>加载内置资源，以下为内置贴图路径</p>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-string">"UI/Skin/UISprite.psd"</span>
<span class="hljs-string">"UI/Skin/Background.psd"</span>
<span class="hljs-string">"UI/Skin/InputFieldBackground.psd"</span>
<span class="hljs-string">"UI/Skin/Knob.psd"</span>
<span class="hljs-string">"UI/Skin/Checkmark.psd"</span>
<span class="hljs-string">"UI/Skin/DropdownArrow.psd"</span>
<span class="hljs-string">"UI/Skin/UIMask.psd"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外还有<code>Runtime</code>还有接口<code>Resources.GetBuiltinResource</code>，但目前没有明确用法</p>
<h2 data-id="heading-1">为什么要将内置资源打包</h2>
<p>若制作多个使用了同样内置资源的 Prefab 且被分到了不同的 Bundle 中，<code>Addressables</code> 的 <code>Default Build Script</code>是不会统计这些引用而单独分包的，会导致内置资源被重复打进不同的 Bundle 中</p>
<p>可通过创建使用<code>Knob</code>和<code>UISprite</code>的 Image Prefab 各两个，并分别打成四个 Bundle</p>
<p><img src="https://dm2305files.storage.live.com/y4m5CCk3VqWJP4vJJct_BCJjkZpBsZ1iCPE8udzn-3X6ov3Xd8cHALXRL2G1POHRJc-f8IGFXnl67an2WRGTPy0LugkwEHDbkx2WD9JgR3MHsD6tnqjd-94T-sWHEs1jChFG2N1dEBF-CvTcupJuR5sU2mPoCsgcGn1LOlutWq8V5H7OFFQoQs_nRZSEkDXdVn5?width=660&height=97&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://dm2305files.storage.live.com/y4mEPfEJk-woS8KbQUtfs_bja5fFfsFnxy9jNJgDMu8ONXWrPQ7E7pVfH-Sn7o1xRRsVBpFl1B3iP757U02svle-eLdMqU7xhf4vIujrXmBLefrSAZu8EHk7492Tu3Kquc_avm3qm3dBdDgBesDsgBm156-wJr71fH7VTwZEax-mFLUgseapNqj7P3VU3qRc-7R?width=250&height=94&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过对四个 Bundle 解包可看到使用相同资源的 Bundle 都有类似如下的内容（<code>Knob</code> 或 <code>UISprite</code>），data 部分就是资源实际的数据内容，被重复打进了两个包</p>
<pre><code class="hljs language-yaml copyable" lang="yaml"><span class="hljs-attr">ID:</span> <span class="hljs-number">5424255917358561739</span> <span class="hljs-string">(ClassID:</span> <span class="hljs-number">213</span><span class="hljs-string">)</span> <span class="hljs-string">Sprite</span>
<span class="hljs-string">m_Name</span> <span class="hljs-string">"Knob"</span> <span class="hljs-string">(string)</span>
<span class="hljs-string">m_Rect</span>  <span class="hljs-string">(Rectf)</span>
<span class="hljs-string">x</span> <span class="hljs-number">12</span> <span class="hljs-string">(float)</span>
<span class="hljs-string">y</span> <span class="hljs-number">12</span> <span class="hljs-string">(float)</span>
<span class="hljs-string">width</span> <span class="hljs-number">40</span> <span class="hljs-string">(float)</span>
<span class="hljs-string">height</span> <span class="hljs-number">40</span> <span class="hljs-string">(float)</span>
<span class="hljs-string">m_Offset</span> <span class="hljs-string">(0</span> <span class="hljs-number">0</span><span class="hljs-string">)</span> <span class="hljs-string">(Vector2f)</span>
<span class="hljs-string">m_Border</span> <span class="hljs-string">(0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">0</span><span class="hljs-string">)</span> <span class="hljs-string">(Vector4f)</span>
<span class="hljs-string">m_PixelsToUnits</span> <span class="hljs-number">200</span> <span class="hljs-string">(float)</span>
<span class="hljs-string">m_Pivot</span> <span class="hljs-string">(0.5</span> <span class="hljs-number">0.5</span><span class="hljs-string">)</span> <span class="hljs-string">(Vector2f)</span>
<span class="hljs-string">m_Extrude</span> <span class="hljs-number">1</span> <span class="hljs-string">(unsigned</span> <span class="hljs-string">int)</span>
<span class="hljs-string">m_IsPolygon</span> <span class="hljs-number">0</span> <span class="hljs-string">(bool)</span>
<span class="hljs-string">m_RenderDataKey</span>  <span class="hljs-string">(pair)</span>
<span class="hljs-string">first</span> <span class="hljs-string">0000000000000000f000000000000000</span> <span class="hljs-string">(GUID)</span>
<span class="hljs-string">second</span> <span class="hljs-number">10913</span> <span class="hljs-string">(SInt64)</span>
<span class="hljs-string">m_AtlasTags</span>  <span class="hljs-string">(vector)</span>
<span class="hljs-string">size</span> <span class="hljs-number">0</span> <span class="hljs-string">(int)</span>
<span class="hljs-string">...............................</span>
<span class="hljs-string">...............................</span>
<span class="hljs-string">size</span> <span class="hljs-number">184</span> <span class="hljs-string">(int)</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#0: 205 204 204 61 205 204 76 61 0 0 0 0 92 143 194 61 205 204 204 189 0 0 0 0 205</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#25: 204 204 61 123 20 174 189 0 0 0 0 123 20 174 61 205 204 204 61 0 0 0 0 205 204</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#50: 76 189 205 204 204 61 0 0 0 0 10 215 163 189 205 204 204 189 0 0 0 0 92 143 194</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#75: 189 41 92 143 61 0 0 0 0 205 204 204 189 143 194 245 60 0 0 0 0 205 204 204 189</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#100: 174 71 97 189 0 0 0 0 0 0 0 0 62 62 62 143 62 62 62 143 62 62 62 143 62</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#125: 62 62 143 62 62 62 143 73 73 73 137 116 116 116 135 146 146 146 94 255 255 255 0 255 255</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#150: 255 0 146 146 146 50 117 117 117 134 55 55 55 143 62 62 62 143 62 62 62 143 62 62 62</span>
<span class="hljs-string">data</span> <span class="hljs-string">(UInt8)</span> <span class="hljs-comment">#175: 143 62 62 62 143 62 62 62 143</span>
<span class="hljs-string">m_Bindpose</span>  <span class="hljs-string">(vector)</span>
<span class="hljs-string">size</span> <span class="hljs-number">0</span> <span class="hljs-string">(int)</span>

<span class="hljs-string">...............................</span>
<span class="hljs-string">...............................</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>此时一个 Bundle 的大小约为 8 KB</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e83592a91294f2090296f4be446e24e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>若内置资源使用范围比较广泛且分包较多，也是有可能造成一定的空间浪费，因此可重写<code>Addressables</code>打包脚本，将使用的内质资源独立打包</p>
<h2 data-id="heading-2">编写 Addressables 打包脚本</h2>
<h3 data-id="heading-3">默认打包脚本</h3>
<p>首先可以查看<code>Addressables</code>的默认打包流程，在<code>Packages/Addressables/Editor/Build/DataBuilders</code>下可找到<code>Addressables</code>提供的几种预设打包模式脚本，其中<code>BuildScriptPackedMode.cs</code>即为<code>Default Build Script</code></p>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-function"><span class="hljs-keyword">static</span> IList<IBuildTask> <span class="hljs-title">RuntimeDataBuildTasks</span>(<span class="hljs-params"><span class="hljs-built_in">string</span> builtinShaderBundleName</span>)</span>
&#123;
    <span class="hljs-keyword">var</span> buildTasks = <span class="hljs-keyword">new</span> List<IBuildTask>();

    <span class="hljs-comment">// Setup</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> SwitchToBuildPlatform());
    buildTasks.Add(<span class="hljs-keyword">new</span> RebuildSpriteAtlasCache());

    <span class="hljs-comment">// Player Scripts</span>
    <span class="hljs-keyword">if</span> (!s_SkipCompilePlayerScripts)
        buildTasks.Add(<span class="hljs-keyword">new</span> BuildPlayerScripts());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostScriptsCallback());

    <span class="hljs-comment">// Dependency</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> CalculateSceneDependencyData());
    buildTasks.Add(<span class="hljs-keyword">new</span> CalculateAssetDependencyData());
    buildTasks.Add(<span class="hljs-keyword">new</span> AddHashToBundleNameTask());
    buildTasks.Add(<span class="hljs-keyword">new</span> StripUnusedSpriteSources());
    buildTasks.Add(<span class="hljs-keyword">new</span> CreateBuiltInShadersBundle(builtinShaderBundleName));
    buildTasks.Add(<span class="hljs-keyword">new</span> PostDependencyCallback());

    <span class="hljs-comment">// Packing</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundlePacking());
    buildTasks.Add(<span class="hljs-keyword">new</span> UpdateBundleObjectLayout());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundleCommands());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateSubAssetPathMaps());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundleMaps());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostPackingCallback());

    <span class="hljs-comment">// Writing</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> WriteSerializedFiles());
    buildTasks.Add(<span class="hljs-keyword">new</span> ArchiveAndCompressBundles());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateLocationListsTask());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostWritingCallback());

    <span class="hljs-keyword">return</span> buildTasks;
&#125;

<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">virtual</span> TResult <span class="hljs-title">DoBuild</span><<span class="hljs-title">TResult</span>>(<span class="hljs-params">AddressablesDataBuilderInput builderInput, AddressableAssetsBuildContext aaContext</span>) <span class="hljs-keyword">where</span> TResult : IDataBuilderResult</span>
&#123;
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-keyword">var</span> builtinShaderBundleName = Hash128.Compute(GetProjectName()) + <span class="hljs-string">"_unitybuiltinshaders.bundle"</span>;
  <span class="hljs-keyword">var</span> buildTasks = RuntimeDataBuildTasks(builtinShaderBundleName);
  buildTasks.Add(extractData);
  
  IBundleBuildResults results;
<span class="hljs-keyword">using</span> (m_Log.ScopedStep(LogLevel.Info, <span class="hljs-string">"ContentPipeline.BuildAssetBundles"</span>))
<span class="hljs-keyword">using</span> (<span class="hljs-keyword">new</span> SBPSettingsOverwriterScope(ProjectConfigData.generateBuildLayout)) <span class="hljs-comment">// build layout generation requires full SBP write results</span>
&#123;
    <span class="hljs-keyword">var</span> exitCode = ContentPipeline.BuildAssetBundles(buildParams, <span class="hljs-keyword">new</span> BundleBuildContent(m_AllBundleInputDefs), <span class="hljs-keyword">out</span> results, buildTasks, aaContext, m_Log);

    <span class="hljs-keyword">if</span> (exitCode < ReturnCode.Success)
        <span class="hljs-keyword">return</span> AddressableAssetBuildResult.CreateResult<TResult>(<span class="hljs-literal">null</span>, <span class="hljs-number">0</span>, <span class="hljs-string">"SBP Error"</span> + exitCode);
   &#125;
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>抛弃代码中对资源的预分析和配置过程，如上代码为开始构建的核心部分，在<code>DoBuild</code>方法中创建构建任务队列，使用<code>ContentPipeline.BuildAssetBundles</code>开始构建打包</p>
<p><code>RuntimeDataBuildTasks</code>任务队列中有一个任务<code>CreateBuiltInShadersBundle</code>的功能是找到打包资源中使用到的内置 Shader 并独立打包，分析其中核心方法</p>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-function"><span class="hljs-keyword">public</span> ReturnCode <span class="hljs-title">Run</span>(<span class="hljs-params"></span>)</span>
&#123;
  <span class="hljs-comment">//获取所有依赖资源中的内置资源，内置资源的GUID都统一为 0000000000000000f000000000000000</span>
    HashSet<ObjectIdentifier> buildInObjects = <span class="hljs-keyword">new</span> HashSet<ObjectIdentifier>();
    <span class="hljs-keyword">foreach</span> (AssetLoadInfo dependencyInfo <span class="hljs-keyword">in</span> m_DependencyData.AssetInfo.Values)
        buildInObjects.UnionWith(dependencyInfo.referencedObjects.Where(x => x.guid == k_BuiltInGuid));

    <span class="hljs-keyword">foreach</span> (SceneDependencyInfo dependencyInfo <span class="hljs-keyword">in</span> m_DependencyData.SceneInfo.Values)
        buildInObjects.UnionWith(dependencyInfo.referencedObjects.Where(x => x.guid == k_BuiltInGuid));

    ObjectIdentifier[] usedSet = buildInObjects.ToArray();
    Type[] usedTypes = BuildCacheUtility.GetTypeForObjects(usedSet);

    <span class="hljs-keyword">if</span> (m_Layout == <span class="hljs-literal">null</span>)
        m_Layout = <span class="hljs-keyword">new</span> BundleExplictObjectLayout();

  <span class="hljs-comment">//从依赖的内置资源中找到所有的 Shader 资源，并记录在指定的 Bundle 名下</span>
    Type shader = <span class="hljs-keyword">typeof</span>(Shader);
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < usedTypes.Length; i++)
    &#123;
        <span class="hljs-keyword">if</span> (usedTypes[i] != shader)
            <span class="hljs-keyword">continue</span>;

        m_Layout.ExplicitObjectLocation.Add(usedSet[i], ShaderBundleName);
    &#125;

    <span class="hljs-keyword">if</span> (m_Layout.ExplicitObjectLocation.Count == <span class="hljs-number">0</span>)
        m_Layout = <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">return</span> ReturnCode.Success;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">脚本改写</h3>
<p>由上述代码可见，默认的打包脚本已经帮助我们筛选出了所有的内置资源，只是额外添加了 Shader 单一类型的筛选，因此直接改造<code>CreateBuiltInShadersBundle</code>即可</p>
<ol>
<li>创建一个新的实现<code>IBUildTask</code>的类 <code>CreateBuiltInBundle</code>，主要代码内容与<code>CreateBuiltInShadersBundle</code>保持一致，构造方法记录两个 Bundle 名ShaderBundleName 和 BundleName ，一个用于打包内置 Shader，一个用于打包其他内置资源，并对做出如下修改</li>
</ol>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-function"><span class="hljs-keyword">public</span> ReturnCode <span class="hljs-title">Run</span>(<span class="hljs-params"></span>)</span>
&#123;
    HashSet<ObjectIdentifier> buildInObjects = <span class="hljs-keyword">new</span> HashSet<ObjectIdentifier>();
    <span class="hljs-keyword">foreach</span> (AssetLoadInfo dependencyInfo <span class="hljs-keyword">in</span> m_DependencyData.AssetInfo.Values)
        buildInObjects.UnionWith(dependencyInfo.referencedObjects.Where(x => x.guid == k_BuiltInGuid));

    <span class="hljs-keyword">foreach</span> (SceneDependencyInfo dependencyInfo <span class="hljs-keyword">in</span> m_DependencyData.SceneInfo.Values)
        buildInObjects.UnionWith(dependencyInfo.referencedObjects.Where(x => x.guid == k_BuiltInGuid));

    ObjectIdentifier[] usedSet = buildInObjects.ToArray();
    Type[] usedTypes = ContentBuildInterface.GetTypeForObjects(usedSet);

    <span class="hljs-keyword">if</span> (m_Layout == <span class="hljs-literal">null</span>)
        m_Layout = <span class="hljs-keyword">new</span> BundleExplictObjectLayout();
    
  <span class="hljs-comment">// 将 Shader 和非 Shader 资源分别记录到两个不同的 Bundle 中</span>
    Type shader = <span class="hljs-keyword">typeof</span>(Shader);
    <span class="hljs-keyword">for</span> (<span class="hljs-built_in">int</span> i = <span class="hljs-number">0</span>; i < usedTypes.Length; i++)
    &#123;
        m_Layout.ExplicitObjectLocation.Add(usedSet[i], usedTypes[i] == shader ? ShaderBundleName : BundleName);
    &#125;

    <span class="hljs-keyword">if</span> (m_Layout.ExplicitObjectLocation.Count == <span class="hljs-number">0</span>)
        m_Layout = <span class="hljs-literal">null</span>;

    <span class="hljs-keyword">return</span> ReturnCode.Success;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>
<p>创建一个新的 Build Script 继承自<code>BuildScriptBase</code>，所有代码和<code>BuildScriptPackedMode.cs</code>保持一致，菜单名称配置可自定义</p>
<p>将<code>RuntimeDataBuildTasks</code>中<code>buildTasks.Add(new CreateBuiltInShadersBundle(builtinShaderBundleName));</code>替换为改造后的<code>CreateBuiltInBundle</code>，并在<code>DoBuild</code>方法中配置 Bundle 名称</p>
</li>
</ol>
<pre><code class="hljs language-c# copyable" lang="c#"><span class="hljs-function"><span class="hljs-keyword">static</span> IList<IBuildTask> <span class="hljs-title">RuntimeDataBuildTasks</span>(<span class="hljs-params"><span class="hljs-built_in">string</span> builtinShaderBundleName, <span class="hljs-built_in">string</span> builtinBundleName</span>)</span>
&#123;
    <span class="hljs-keyword">var</span> buildTasks = <span class="hljs-keyword">new</span> List<IBuildTask>();

    <span class="hljs-comment">// Setup</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> SwitchToBuildPlatform());
    buildTasks.Add(<span class="hljs-keyword">new</span> RebuildSpriteAtlasCache());

    <span class="hljs-comment">// Player Scripts</span>
    <span class="hljs-keyword">if</span> (!s_SkipCompilePlayerScripts)
        buildTasks.Add(<span class="hljs-keyword">new</span> BuildPlayerScripts());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostScriptsCallback());

    <span class="hljs-comment">// Dependency</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> CalculateSceneDependencyData());
    buildTasks.Add(<span class="hljs-keyword">new</span> CalculateAssetDependencyData());
    buildTasks.Add(<span class="hljs-keyword">new</span> AddHashToBundleNameTask());
    buildTasks.Add(<span class="hljs-keyword">new</span> StripUnusedSpriteSources());
    buildTasks.Add(<span class="hljs-keyword">new</span> CreateBuiltInBundle(builtinShaderBundleName, builtinBundleName));
    buildTasks.Add(<span class="hljs-keyword">new</span> PostDependencyCallback());

    <span class="hljs-comment">// Packing</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundlePacking());
    buildTasks.Add(<span class="hljs-keyword">new</span> UpdateBundleObjectLayout());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundleCommands());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateSubAssetPathMaps());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateBundleMaps());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostPackingCallback());

    <span class="hljs-comment">// Writing</span>
    buildTasks.Add(<span class="hljs-keyword">new</span> WriteSerializedFiles());
    buildTasks.Add(<span class="hljs-keyword">new</span> ArchiveAndCompressBundles());
    buildTasks.Add(<span class="hljs-keyword">new</span> GenerateLocationListsTask());
    buildTasks.Add(<span class="hljs-keyword">new</span> PostWritingCallback());

    <span class="hljs-keyword">return</span> buildTasks;
&#125;

<span class="hljs-function"><span class="hljs-keyword">protected</span> <span class="hljs-keyword">virtual</span> TResult <span class="hljs-title">DoBuild</span><<span class="hljs-title">TResult</span>>(<span class="hljs-params">AddressablesDataBuilderInput builderInput, AddressableAssetsBuildContext aaContext</span>) <span class="hljs-keyword">where</span> TResult : IDataBuilderResult</span>
&#123;
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-keyword">var</span> builtinBundleName = Hash128.Compute(GetProjectName()) + <span class="hljs-string">"_unitybuiltin.bundle"</span>;
  <span class="hljs-keyword">var</span> builtinShadersBundleName = Hash128.Compute(GetProjectName()) + <span class="hljs-string">"_unitybuiltinshaders.bundle"</span>;
  <span class="hljs-keyword">var</span> buildTasks = RuntimeDataBuildTasks(builtinShadersBundleName, builtinBundleName);
  buildTasks.Add(extractData);
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
  <span class="hljs-comment"><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span><span class="hljs-doctag">///</span>/</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">修改效果</h3>
<p>构建 Bundle 后，多出一个大小为 7 KB 的<code>defaultlocalgroup_unitybuiltin.bundle</code>，通过解包可见其中只有之前重复打包的 Knob 和 UISprite 两个内置资源，而之前的四个 Bundle 已不再包含具体的资源数据，仅包含一段简单的引用数据，同时单个包体的大小由之前的 8 KB 减小为 4 KB</p>
<p><img src="https://dm2305files.storage.live.com/y4m22aT96FBcaXS7Me9PNsVL4_lLHvZ_g_e5n5M5xMOM-3sNhGBVVjPCwpWcBwg89K_geOSR0VSjZkQ3ifM1XSctveiU1sGN_858IXyFO05UOmKbMB9U_XqvgNBa2COYNqCtJSvcMxn9-KSED_BaM-29RXZt6g1UlpBI63ocFWArwAolwQnouqLdXExFXivZtOV?width=460&height=249&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"></p>

























<table><thead><tr><th></th><th>Builtin 打包前</th><th>Builtin 打包后</th></tr></thead><tbody><tr><td>Bundle 数量</td><td>4</td><td>5</td></tr><tr><td>总 Bundle 大小</td><td>32 KB</td><td>22 KB</td></tr><tr><td>单个包体大小</td><td><img src="https://dm2305files.storage.live.com/y4mw4QLA-S-gsZfqty-t1N9Ogqlz5WSt1vHKSwuSQ4lCtU0Zmg41YydeuRUuBTyf9s3CAzP4LCKnWHvM_0R0XaBzRIm0AJABLawCMhY97SBmENonuMv0R7AHma9Dz6BGHSOQolxJ4JYHDDJH9jjolhHe6ow7tjg5ERB3pW8n3svGUPJ-bYJpAKm1o9IgzJ7kSe0?width=328&height=288&cropmode=none" alt loading="lazy" referrerpolicy="no-referrer"></td><td><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b177fffc9da4d5bbf479d2d975cd65d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></td></tr></tbody></table>
<p>源码链接：<a href="https://github.com/Warl-G/GRUnityTools/tree/GRTools.Addressables/Editor/PackScrips" target="_blank" rel="nofollow noopener noreferrer">GRTools.Addressables · Warl-G</a></p>
<h2 data-id="heading-6">参考</h2>
<p><a href="https://zhuanlan.zhihu.com/p/372926245" target="_blank" rel="nofollow noopener noreferrer">Unity内置资源如何打包避免冗余 - 知乎 (zhihu.com)</a></p></div>  
</div>
            