
---
title: 'react-i18next基本使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9661'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 00:59:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=9661'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">配置文件</h3>
<pre><code class="copyable">import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import i18next from 'i18next';
import &#123; initReactI18next &#125; from 'react-i18next';
import intervalPlural from 'i18next-intervalplural-postprocessor';

const useSuspense = process.env.JEST_WORKER_ID ? false : true;

const i18n = i18next
  .use(Backend)
  .use(LanguageDetector)
  .use(initReactI18next)
  .use(intervalPlural)
  .init(
    &#123;
      // load的namespace
      ns: ['common', 'app'],
      // 默认会去查找的namespace
      // 相同的key值，会优先去app命名空间中查找，若没有，才去common
      defaultNS: 'app',
      // i18next-xhr-backend 配置项
      backend: &#123;
        loadPath: '&#123;&#123;ns&#125;&#125;.&#123;&#123;lng&#125;&#125;.json',
        addPath: 'locales/add/&#123;&#123;ns&#125;&#125;.&#123;&#123;lng&#125;&#125;',
      &#125;,
      // i18next-browser-languagedetector 配置项
      detection: &#123;
        order: ['querystring', 'localStorage', 'navigator'],
        caches: ['localStorage'],
        lookupQuerystring: 'language',
        lookupLocalStorage: 'language',
      &#125;,
      // 如果用户选择的语言不被支持，那么使用英文来渲染界面
      fallbackLng: ['en-US', 'zh-CN'],

      interpolation: &#123;
        escapeValue: false, // not needed for react!!
        format: function(value, format, lng) &#123;
            if (format === 'uppercase') return value.toUpperCase();
            if(value instanceof Date) return moment(value).format(format);
            return value;
        &#125;
      &#125;,
      react: &#123;
        wait: true,
        useSuspense: useSuspense,
      &#125;,
      whitelist: ['en-US', 'zh-CN'],
      saveMissing: true,
    &#125;,
    (error, t) => &#123;
      if (!error) &#123;
        document.title = t('app.document.title');
      &#125;
    &#125;
  );

i18n.on('languageChanged', (language) => &#123;
  console.log(language);
  document.title = i18n.t('document.title');
&#125;);

i18n.on('missingKey', (lngs, namespace, key, res) => &#123;
  console.log(key);
&#125;);

export default i18n;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">解释</h3>
<ul>
<li>intervalPlural插件</li>
</ul>
<p>用于区间的数量表示；
利用<code>count</code>属性可以表示复数，但若要区分某个区间，那么需要使用该插件
具体使用见官方用例即可</p>
<ul>
<li>Backend插件</li>
</ul>
<p>由于配置项缺乏resources，所以会触发backend请求，从fetch请求里拿到resources文件<br>
分析backend配置项，loadPath是fetch请求的url,addPath何时触发不知道</p>
<ul>
<li>LanguageDetector插件</li>
</ul>
<p>用于语言检测；可设置检测优先级</p>
<ul>
<li>interpolation</li>
</ul>
<ol>
<li>设置escapeValue为false是取消转义，因为react本身有该功能</li>
<li>设置format格式，展示大写和Date格式</li>
</ol>
<ul>
<li>languageChanged</li>
</ul>
<p>语言改变时会触发的事件，可以在这里改变document.title</p>
<ul>
<li>missingKey</li>
</ul>
<p>当代码中出现资源里没有的key时，会触发该事件；需要注意的是，如果是动态加载页面，只有该页面加载时才会检查</p>
<h3 data-id="heading-2">其他</h3>
<h4 data-id="heading-3">复数</h4>
<ul>
<li>i18n自带复数功能，但要注意，其语言(即)为英文时才生效！<code>中文不生效！</code>；其他语言不知道<br></li>
</ul>
<p>这里的语言一定要是<code>i18n里的language值</code>，如果只是简单把resources文件里的语言写成英文，也不会生效的<br></p>
<pre><code class="copyable">  "key": "item",
  "key_plural": "items",
  
  i18next.t('key', &#123;count: 0&#125;); // -> "items"
  i18next.t('key', &#123;count: 1&#125;); // -> "item"
  i18next.t('key', &#123;count: 5&#125;); // -> "items"
  i18next.t('key', &#123;count: 00&#125;); // -> 报错
<span class="copy-code-btn">复制代码</span></code></pre>
<p>plural前的分割符默认是<code>_</code>，可通过<code>pluralSeparator</code>配置修改<br></p>
<ul>
<li>若想区间复数，那么使用插件intervalPlural，如2-4个item均显示<code>a few items</code></li>
</ul>
<pre><code class="copyable">&#123;
  "key": "&#123;&#123;count&#125;&#125; item",
  "key_plural": "&#123;&#123;count&#125;&#125; items",
  "key_interval": "(1)&#123;one item&#125;;(2-7)&#123;a few items&#125;;(7-inf)&#123;a lot of items&#125;;",
&#125;
i18next.t('key1_interval', &#123;postProcess: 'interval', count: 1&#125;); // -> "one item"
i18next.t('key1_interval', &#123;postProcess: 'interval', count: 4&#125;); // -> "a few items"
i18next.t('key1_interval', &#123;postProcess: 'interval', count: 100&#125;); // -> "a lot of items"
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">key值插入</h4>
<ul>
<li>若想在翻译中，使用变量，那么使用自带Nesting功能即可</li>
</ul>
<pre><code class="copyable">&#123;
    "nesting1": "1 $t(nesting2)",
    "nesting2": "2 $t(nesting3)",
    "nesting3": "3",
&#125;

i18next.t('nesting1'); // -> "1 2 3"
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>此方法可与复数功结合使用</li>
</ul>
<pre><code class="copyable">&#123;
  "time": "$t(hours,&#123;\"count\":&#123;&#123;hours&#125;&#125;&#125;) $t(minutes, &#123;\"count\":&#123;&#123;minutes&#125;&#125;&#125;)",
  "hours": "&#123;&#123;count&#125;&#125; hour",
  "hours_plural": "&#123;&#123;count&#125;&#125; hours",
  "minutes": "&#123;&#123;count&#125;&#125; minute",
  "minutes_plural": "&#123;&#123;count&#125;&#125; minutes",
&#125;
i18next.t('time', &#123; hours: 3, minutes: 2 &#125;) // -> "3 hours 2 minutes"
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            