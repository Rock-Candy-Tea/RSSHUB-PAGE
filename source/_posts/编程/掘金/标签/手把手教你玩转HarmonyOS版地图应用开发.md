
---
title: '手把手教你玩转HarmonyOS版地图应用开发'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb13b2bb57884b8aab9adecb2f2c9419~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:34:47 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb13b2bb57884b8aab9adecb2f2c9419~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>​一、导读</strong></p>
<p>7月31日，华为HarmonyOS开发者日将在杭州举行。为了方便更多开发者，高德开放平台地图SDK已在业内率先实现鸿蒙化迁移和重构，<strong>全面适配HarmonyOS并面向开发者免费发布</strong>。开发者可到高德开放平台官网了解更多内容，获取版本下载、开发文档、常见问题等支持。</p>
<p>访问高德开放平台：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/" ref="nofollow noopener noreferrer">lbs.amap.com/</a></p>
<p>在今年6月2日，华为就正式发布了HarmonyOS。由于HarmonyOS在兼容Android上有特殊要求，如果APP应用是用Android API开发，开发者可以直接使用Android的SDK。</p>
<p>但如果APP用了HarmonyOS的API开发，就不能用Android的SDK而需要使用HarmonyOS版本的SDK。</p>
<p>为了方便开发者在HarmonyOS的相应设备中进行LBS服务的开发，高德开放平台率先进行了HarmonyOS适配，首批适配范围包括地图和搜索SDK，支持嵌入搭载HarmonyOS的手机、Pad及其他智能终端设备。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb13b2bb57884b8aab9adecb2f2c9419~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>二、HarmonyOS地图SDK特性介绍</strong></p>
<p><strong>与高德开放平台Android地图SDK平滑切换</strong></p>
<ul>
<li>
<p>已集成高德开放平台Android地图SDK的开发者可无缝切换到HarmonyOS地图SDK，无额外开发量。HarmonyOS与Android系统间的接口变化由高德开放平台SDK适配层消化，SDK对外接口保持不变。</p>
</li>
<li>
<p>高德底层引擎对接HarmonyOS NDK，上层代码全面对接HarmonyOS SDK，所有系统接口均使用HarmonyOS API。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d19d2be1211b47188ebfb61fe5847315~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>继承高德开放平台Android/iOS地图SDK功能亮点</strong></p>
<ul>
<li>
<p>开发者可以通过高德开放平台API和SDK，轻松完成地图的构建工作，将地图精致地呈现在您的应用中。地图SDK不仅提供丰富的地图覆盖物绘制能力，也支持搜索、多种路径规划、坐标转换、距离测量、面积计算等功能。</p>
</li>
<li>
<p>适配HarmonyOS后的地图SDK依旧支持与自定义地图SaaS平台等周边工具配合使用，开发者可以在平台中定制区域面、建筑物、水系、天空、道路、标注、行政边界共7大类40余种地图元素，灵活设计心仪的地图样式。更多地图SDK基础能力、自定义、可视化能力详情请参考高德开放平台官网。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d77173d1f914d30a18fc7adc7a6ec8b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>HarmonyOS版地图SDK整体框架</strong></p>
<p>HarmonyOS和Android系统差异很大，几乎所有的API都有调整，不少API都调整了实现方案，所以不能通过改包名来实现适配。我们将原生SDK中所有调用Android的代码均切换为适配层，在适配层将SDK的接口一一适配到HarmonyOS接口。</p>
<p>HarmonyOS版地图SDK整体框架大致如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e7cb0d6f1ce4f67ae7a28669febe701~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>三、如何集成-从零开始</strong></p>
<p><strong>第一步 搭建HarmonyOS开发环境</strong></p>
<p>完成DevEco Studio安装、环境配置和工程创建，参考HarmonyOS官网说明：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.harmonyos.com%2Fcn%2Fdocs%2Fdocumentation%2Fdoc-guides%2Fstart-overview-000000000002960" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.harmonyos.com/cn/docs/documentation/doc-guides/start-overview-000000000002960" ref="nofollow noopener noreferrer">developer.harmonyos.com/cn/docs/doc…</a></p>
<p><strong>第二步 配置应用的签名信息</strong></p>
<p>应用工程创建完成后，需要配置签名信息，才可以使用真机调试和发布应用。</p>
<p><strong>第三步 获取应用的appId</strong></p>
<p>配置完签名信息之后，就可以获取当前应用的appId了，这个appId主要用于申请高德的apiKey，请确定最终发布应用的appId，防止最终高德SDK鉴权失败。</p>
<p>通过代码获取应用的appId方式如下：</p>
<pre><code class="copyable">getApplicationContext().getBundleManager().getBundleInfo(getBundleName(), 0).getAppId()
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>注意</strong>：目前通过DevEco Studio连接云真机获取到的appId不全，只获取到了"包名_", 使用云真机调试高德地图SDK时会导致鉴权不通过。正确的appId形式为："包名_签名信息"， 例如：com.amap.demo_BGtGgVB3ASqU7XXXXV2/zhoYh6tFQHAd5DASWVTEAgvZfzrEGljjs=</p>
<p><strong>第四步 在高德开放平台官网控制台申请API Key</strong></p>
<p><strong>创建新应用</strong></p>
<p>从开放平台官网右上角入口-控制台，创建一个新应用。如果您之前已经创建过应用，可直接跳过这个步骤。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f0dd1f1ef4048d7850f1a701c694e70~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1be075fec6a0454c8e36de4245c8bbe2~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>添加新Key</strong></p>
<p>在创建的应用上点击"添加新Key"按钮，在弹出的对话框中，依次：输入应用名名称，选择绑定的服务为“Harmony平台SDK”，输入AppID，如下图所示：</p>
<p>需要注意：1个Key只能用于一个应用（多渠道安装包属于多个应用），1个Key在多个应用上使用会出现服务调用失败。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/562154f8a2844c75a6e884d6443c4841~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在阅读完高德地图API服务条款后，勾选此选项，点击“提交”，完成Key的申请，此时您可以在所创建的应用下面看到刚申请的Key了。</p>
<p><strong>第五步 在代码中设置申请的Key</strong></p>
<p>请使用API的方式将申请的高德API Key设置给高德地图SDK。</p>
<pre><code class="copyable">/**
 * 动态设置apiKey。
 *
 * @param apiKey 在高德官网上申请的apiKey。
 */
MapsInitializer.setApiKey(String apiKey)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：请确保在调用任何高德地图SDK的接口之前将API Key设置给高德地图SDK，建议放到Application的初始化之中。</p>
<p>完成以上5步之后，就可以愉快的使用HarmonyOS版高德地图SDK了。</p>
<p><strong>四、如何使用-创建地图</strong></p>
<p>使用地图SDK之前，需要在config.json文件中进行相关权限设置，确保地图功能可以正常使用。</p>
<p><strong>第一步 配置config.json</strong></p>
<p>首先，声明权限。</p>
<pre><code class="copyable">...
"reqPermissions": [
      &#123;
        "usedScene": &#123;
          "ability": [
            "com.example.harmonysearchsdk.MainAbility"
          ],
          "when": "always"
        &#125;,
        "reason": "request internet",
        "name": "ohos.permission.INTERNET"
      &#125;
    ]
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第二步 向工程中添加地图开发包</strong></p>
<p>将har包放入libs目录下，依次添加依赖。</p>
<pre><code class="copyable">dependencies &#123;
    implementation files("libs/xxx.har")
    //...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>或者直接使用引入libs下所有har包的方式：</p>
<pre><code class="copyable">dependencies &#123;
  implementation fileTree(dir: 'libs', include: ['*.jar', '*.har'])
    //...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>第三步 初始化地图容器</strong></p>
<p><strong>设置Key</strong></p>
<p>获取Key方式请参考上方“从零开始”章节第四步。</p>
<pre><code class="copyable">MapsInitializer.setApiKey("您的key");
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建MapView</strong></p>
<pre><code class="copyable">public class BasicMapDemoSlice extends Ability &#123;

    private MapView mapView;

    @Override
    protected void onStart(Intent intent) &#123;
        super.onStart(intent);
        initMapView();
    &#125;

    private void initMapView() &#123;
        mapView = new MapView(this);

        mapView.onCreate(null);
        mapView.onResume();
        DirectionalLayout.LayoutConfig config = new DirectionalLayout.LayoutConfig(
                DirectionalLayout.LayoutConfig.MATCH_PARENT, DirectionalLayout.LayoutConfig.MATCH_PARENT);
        mapView.setLayoutConfig(config);
        super.setUIContent(mapView);
    &#125;

    @Override
    protected void onStop() &#123;
        super.onStop();
        if (mapView != null) &#123;
            mapView.onDestroy();
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>初始化地图并获取AMap对象</strong></p>
<pre><code class="copyable">AMap aMap = mapView.getMap();
aMap.setOnMapLoadedListener(new AMap.OnMapLoadedListener() &#123;
    @Override
    public void onMapLoaded() &#123;
    // todo
    &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此就可以看到地图展示，并且拿到AMap对象后，就可以往地图上添加点线面等覆盖物了。</p>
<p><strong>五、获取更多详情和开发支持</strong></p>
<p>访问高德开放平台：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/" ref="nofollow noopener noreferrer">lbs.amap.com/</a></p>
<p>获取HarmonyOS版高德地图SDK下载、开发文档、Demo等开发支持：<a href="https://link.juejin.cn/?target=https%3A%2F%2Flbs.amap.com%2Fapi%2Fharmonyos-sdk%2Fsummary%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://lbs.amap.com/api/harmonyos-sdk/summary/" ref="nofollow noopener noreferrer">lbs.amap.com/api/harmony…</a></p></div>  
</div>
            