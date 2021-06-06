
---
title: 'React Native入门笔记'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6183'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 23:39:33 GMT
thumbnail: 'https://picsum.photos/400/300?random=6183'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><h1 data-id="heading-0">React Native 笔记</h1>
<h3 data-id="heading-1">vscode 插件</h3>
<ul>
<li>Prettier - Code formatter</li>
<li>Simple React Snippets</li>
</ul>
<h3 data-id="heading-2">React Native 基础命令</h3>
<pre><code class="copyable">#打开手机debug模式
adb shell input keyevent 82

# React Native 脚手架
npm install -g react-native-cli

#初始化一个新的项目
npx react-native init your-app 

cd AwesomeProject
yarn android
# 或者
yarn react-native run-android

# 启动项目
npx react-native run-android
#查看设备
adb devices  

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">小技巧</h3>
<p>修改入口文件<code>index.js</code></p>
<ul>
<li>在 netWork 查看网络请求</li>
</ul>
<blockquote>
<p>GLOBAL.originalXMLHttpRequest 引用 XHR 的 Chrome 开发工具副本。由 RN 提供，作为逃生舱口。Shvetusya 的解决方案仅在开发工具处于打开状态并提供 XMLHttpRequest 时才有效。</p>
</blockquote>
<pre><code class="copyable">GLOBAL.XMLHttpRequest = GLOBAL.originalXMLHttpRequest || GLOBAL.XMLHttpRequest;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>关闭黄色警告</li>
</ul>
<pre><code class="copyable">// 关闭黄色警告
console.ignoredYellowBox = ['Warning: BackAndroid is deprecated. Please use BackHandler instead.','source.uri should not be an empty string','Invalid props.style key'];
console.disableYellowBox = true // 关闭全部黄色警告

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">常用组件汇总</h3>
<p><a href="https://www.jianshu.com/p/53ff78168acc" target="_blank" rel="nofollow noopener noreferrer">www.jianshu.com/p/53ff78168…</a></p>
<p><a href="https://reactnative.dev/docs/more-resources" target="_blank" rel="nofollow noopener noreferrer">reactnative.dev/docs/more-r…</a></p>
<h1 data-id="heading-5">设计稿 单位转换为手机</h1>
<ul>
<li>公式</li>
</ul>
<blockquote>
<p>设计稿宽度 / 元素的宽度 = 手机屏幕的宽度 / 手机中元素的宽度</p>
</blockquote>
<p>手机中元素的宽度 = 手机屏幕的宽度 * 元素的宽度 / 设计稿的宽度</p>
<h3 data-id="heading-6">Genymotion 报错</h3>
<p><a href="https://www.cnblogs.com/shizk/p/11189978.html" target="_blank" rel="nofollow noopener noreferrer">react-native 启动时红屏报错：Unable to load script.Make sure you’re either running a metro server or that …</a></p>
<pre><code class="copyable">react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res 

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">打包 APK</h3>
<p><a href="https://reactnative.cn/docs/signed-apk-android" target="_blank" rel="nofollow noopener noreferrer">打包 APK</a><br>
<a href="https://blog.csdn.net/hssdw25172008/article/details/8499423" target="_blank" rel="nofollow noopener noreferrer">keytool 错误: java.io.FileNotFoundException: MyAndroidKey.keystore (拒绝访问).</a></p>
<pre><code class="copyable">.\keytool -genkeypair -v -keystore d:/social_app.keystore -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Warning:<br>
JKS 密钥库使用专用格式。建议使用 “keytool -importkeystore -srckeystore d:/my-release-key.keystore -destkeystore d:/my-release-key.keystore -deststoretype pkcs12” 迁移到行业标准格式 PKCS12。</li>
</ul>
<h3 data-id="heading-8">React Native Component ExceptionElement</h3>
<p>[外链图片转存失败, 源站可能有防盗链机制, 建议将图片保存下来直接上传 (img-ams5tL6S-1616911604903)(./Component_Excepthon.png)]</p>
<ul>
<li>在引入组件时不要 加 &#123;&#125;</li>
</ul>
<h4 data-id="heading-9">参考</h4>
<p><a href="https://stackoverflow.com/questions/65100627/react-native-component-exception-element-type-is-invalid-expected-string-go" target="_blank" rel="nofollow noopener noreferrer">React Native Component Exception - Element Type is invalid: expected string…got undefined</a></p></div>  
</div>
            