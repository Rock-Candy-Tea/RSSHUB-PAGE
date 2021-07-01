
---
title: 'Capacitor基于angular框架的NFC的Android插件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2237'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 18:58:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=2237'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">cap-nfc-plugin</h1>
<h2 data-id="heading-1">Description</h2>
<pre><code class="copyable">这是一款Capacitor基于angular框架的NFC的Android插件
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">Installing</h2>
<hr>
<pre><code class="copyable">$ npm i cap-nfc-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">Methods</h2>
<hr>
<ul>
<li>监听读取NFC信息: <code>NFCPlugin.addListener('readNFCResult',callback)</code></li>
<li>监听开始写入NFC: <code>NFCPlugin.addListener('beginWriteNFC',callback)</code></li>
<li>监听写入NFC成功或失败的结果: <code>NFCPlugin.addListener('writeNFCResult',callback)</code></li>
<li>NFC开始读写后,向android发送任务信息: <code>NFCPlugin.sendTaskInfo(&#123;taskInfo: Object&#125;)</code></li>
</ul>
<h2 data-id="heading-4">Usage</h2>
<hr>
<p>Import the plugin you want to use into your x.component.ts file .</p>
<pre><code class="copyable">import &#123; Plugins, Capacitor &#125; from '@capacitor/core';
const &#123; NFCPlugin &#125; = Plugins;
@Component(&#123;
  selector: 'x',
  templateUrl: './x.component.html'
&#125;)

export class AppComponent implements AfterViewInit &#123; 
    ngAfterViewInit(): void &#123;
        NFCPlugin.addListener('readNFCResult', (info: any) => &#123;
          console.log('readNFCResult was fired', info);
        &#125;);
        NFCPlugin.addListener('beginWriteNFC', (info: any) => &#123;
          console.log('beginWriteNFC was fired', info);
        &#125;);
        NFCPlugin.addListener('writeNFCResult', (info: any) => &#123;
          console.log('writeNFCResult was fired', info);
        &#125;);
    &#125;
    
     sendTaskInfo() &#123;
        NFCPlugin.sendTaskInfo(&#123;
          taskInfo: &#123;
            id: 1,
            taskNumber: "111111",
            process: "joy",
          &#125;,
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">Update Your Project</h2>
<hr>
<p>just running command</p>
<pre><code class="copyable">npm run android
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">Upgrade Plugin</h2>
<hr>
<ol>
<li>
<p><code>delete current project's node_modules folder and android folder</code></p>
</li>
<li>
<p><code>npm i</code></p>
</li>
<li>
<p><code>npm i cap-nfc-plugin@latest</code></p>
</li>
<li>
<p><code>npx cap add android</code></p>
</li>
<li>
<p><code>npm run android</code></p>
</li>
<li>
<p>到此步骤会自动打开Android studio, 找到<code>MainActivity.java</code>文件</p>
</li>
<li>
<p>将Plugin添加到mainActivity中</p>
<pre><code class="copyable">public class MainActivity extends BridgeActivity &#123;
  @Override
  public void onCreate(Bundle savedInstanceState) &#123;
    super.onCreate(savedInstanceState);

    // Initializes the Bridge
    this.init(savedInstanceState, new ArrayList<Class<? extends Plugin>>() &#123;&#123;
      // Additional plugins you've installed go here
      // Ex: add(TotallyAwesomePlugin.class);
      add(NFCPlugin.class);
    &#125;&#125;);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>找到<code>app/manifests/AndroidManifest.xml</code>文件，将<code>android:usesCleartextTraffic="true"</code>添加到<code>application</code>中</p>
<pre><code class="copyable"> <application
     android:allowBackup="true"
     android:icon="@mipmap/ic_launcher"
     android:label="@string/app_name"
     android:roundIcon="@mipmap/ic_launcher_round"
     android:supportsRtl="true"
     android:usesCleartextTraffic="true"
     android:theme="@style/AppTheme">
     
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>现在可以打包出来啦，Finished</p>
</li>
</ol>
<h2 data-id="heading-7">Debugger In Chrome</h2>
<hr>
<p>open url <code>chrome://inspect/#devices</code> in chrome, you can find device in it</p></div>  
</div>
            