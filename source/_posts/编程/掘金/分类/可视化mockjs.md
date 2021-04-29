
---
title: '可视化mockjs'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3df94e339a40378f46ad2c5208b352~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Apr 2021 17:39:59 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3df94e339a40378f46ad2c5208b352~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>Mock就是用一个虚拟的对象（Mock 对象）来创建以便测试的测试方法。</p>
<ul>
<li>随着WEB技术的发展，前后端分离架构变得普遍起来，但是问题也随之而来，文档零散、不规范。并且经常碰到例如参数的新增、变动。这就导致了后端工程师需要耗费大量的时间维护接口文档</li>
<li>前端的开发工作依赖于后端提供的接口数据，但是后端接口往往没有那么快就可以开发完成。这就导致了前端在“等”数据。</li>
<li>上述的情况就会导致工作效率低下，沟通成本增加。接口管理平台的需求就日趋强烈</li>
</ul>
<p>所以这也促进了mock的出现和发展</p>
<h3 data-id="heading-1">说说自己使用mock的变化</h3>
<h4 data-id="heading-2">1.原地模拟数据</h4>
<p>直接在页面data里面声明或者外部文件声明然后引入
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca3df94e339a40378f46ad2c5208b352~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7502ca8b1e844dc2be3c7ea4bc89192b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>优点：这样相应页面就会有占位数据，有个直观的感觉</p>
<p>缺点：数据写死，不会变化，也不是从接口获取 后期待对接的工作量还是很高，而且前期成本也不低</p>
<h4 data-id="heading-3">2.接口声明return数据</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53e45729da444c3686c9cf60a8b9afcf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这里其实和第一种没什么区别，在接口定义的地方返回数据。只是起到占位的作用，非要和第一个对比，只是增加了接口简单声明，为后面对接少了一点点工作量，其实后面对接，还是有很多工作要做。</p>
<h4 data-id="heading-4">3.使用mock.js</h4>
<p>其实较早接触mock.js 最近才知道YApi
直接模拟相应接口返回，接口名也可以自定义，数据类型也可以自定义 随意改动等等好处
在下一步慢慢体会
直接使用引入mockjs然后使用</p>
<pre><code class="copyable">const ResultUtil = require('../_util/resultUtil');
const Mock = require('mockjs');
// 公告管理
const dataList = Mock.mock(&#123;
  'rows|12': [
    &#123;
      demoId: '@id',
      demoTitle: '@ctitle(3,10)',
      demoCnte: '<h2 style="text-align: center;">公告</h2><p>测试测试，内容内容。</p>',
      'demoMan|1': ['张三', '李四'],
      demoTime: '@datetime',
      'demoStatusText|1': ['生效', '未生效'],
      'demoStatus|1': ['1', '2'],

      'demoRole|1': ['1', '2'],
      'demoRoleText|1': ['专家', '社会监督员'],
      'demoMethod|1': ['1', '2'],
      'demoMethodText|1': ['PC', '微信'],
      demoFileList: [
        &#123;
          archiveFor: 'xls',
          archiveId: 107,
          archiveName: '任务管理病案审核专家意见模板.xls',
          bizId: 'ZJYY0001',
          cldArchiveId: '557',
          crteTime: 1606443355672,
          crterId: '0',
          crterName: '超级管理员',
          fileBase64: null,
          matId: '1303',
          rid: '557',
          updtTime: 1606443355672,
          valiFlag: null,
        &#125;,
      ],
    &#125;,
  ],
&#125;);
// 操作历史
const hisList = Mock.mock(&#123;
  'rows|32': [
    &#123;
      hisId: '@id',
      hisResult: '@ctitle(3,40)',
      'hisName|1': ['张三', '李四'],
      hisTime: '@datetime',
      'hisTypeStatusText|1': ['生效', '未生效'],
      'hisTypeStatus|1': ['1', '2'],
      'opterRoleText|1': ['专家', '社会监督员'],
    &#125;,
  ],
&#125;);

module.exports = &#123;
  // 查询列表
  'GET /demo/getList 500': (&#123; query &#125;) => &#123;
    const &#123; pageNo = 1, pageSize = 10 &#125; = query;
    const dataListItems = dataList.rows;
    const pageData = ResultUtil.pagination(pageNo, pageSize, dataListItems);
    return ResultUtil.pageSuccess(pageData, dataListItems.length);
  &#125;,
  // 查询详情
  'GET /demo/detail 500': (&#123; query &#125;) => &#123;
    const &#123; demoId = '' &#125; = query;
    const dataListItems = dataList.rows;
    const index = dataListItems.findIndex((item) => item.demoId === demoId);
    return ResultUtil.success(dataListItems[index !== -1 ? index : 0]);
  &#125;,
  //   查询历史记录
  'GET /demo/getHistory 500': (&#123; query &#125;) => &#123;
    const &#123; pageNo = 1, pageSize = 10 &#125; = query;
    const dataListItems = hisList.rows;
    const pageData = ResultUtil.pagination(pageNo, pageSize, dataListItems);
    return ResultUtil.pageSuccess(pageData, dataListItems.length);
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样的话在项目中就可以像调用接口 然后去模拟随机生成数组，mockjs很强大 我也没全懂，具体详情官网奉上 <a href="http://mockjs.com/0.1/#" target="_blank" rel="nofollow noopener noreferrer">mock官方文档</a> 和 <a href="https://github.com/nuysoft/Mock" target="_blank" rel="nofollow noopener noreferrer">项目地址</a></p>
<p>这样的做法也是我之前的做法 我在使用的时候就在想 能不能更简单的去配置类似<a href="https://github.com/thx/rap2-delos" target="_blank" rel="nofollow noopener noreferrer">rap2</a>或者<a href="https://github.com/easy-mock/easy-mock" target="_blank" rel="nofollow noopener noreferrer">easy-mock</a>大搜车这样 可视化操作。
如果你是团队多人 我也建议在这样的网站上拉个团队建个仓库 多人协调工作</p>
<p>那我个人玩玩 接下来介绍本文重点-<a href="https://github.com/wangxiaoer5200/serve-mock" target="_blank" rel="nofollow noopener noreferrer">一个本地化的可视化配置的mock项目</a></p>
<h3 data-id="heading-5">项目介绍</h3>
<p>一个基于mockjs、vue2、koa实现一个本地化的可视化配置的服务项目(<code>本文大篇幅介绍，也是本文最想表达的项目详情</code>)</p>
<ul>
<li><a href="https://github.com/wangxiaoer5200/serve-mock" target="_blank" rel="nofollow noopener noreferrer">github项目地址</a></li>
<li><a href="https://gitee.com/wangxiaoer520/mock-serve-demo" target="_blank" rel="nofollow noopener noreferrer">gitee项目地址</a></li>
</ul>
<h4 data-id="heading-6">1.项目结构</h4>
<p>一个page是ui界面的项目
一个server是本地接口服务项目</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8db4d40b440e4394b3cf2cc17df00f5f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">2.项目运行</h4>
<p>首先page和server都要安装依赖
先把服务跑起来 然后再跑page</p>
<pre><code class="copyable">// 命令1
cd page
yarn 
yarn run serve
// 命令2
cd server
yarn 
yarn run serve

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13fa287649b14f009ae369373946ef23~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/886e60aaa8684e3d90d6183926d5428f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">3.项目使用</h4>
<p>这是跑起来的ui界面
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea032db8cc554b91904caa5bf6e2daf3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
你在这可以去添加各种模块和接口，然后自定义返回类型
添加成功可以直接浏览器测试或者点测试接口  也可以在项目中使用
注意点：如果你接口有参数之类是要相应填写的</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51745b0f6e4a4c50b2d7c3e50a4b38b5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/902f4b8cd0de4f95afe2b31286aa2770~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用的话 知道操作后就特别的流畅方便 一开始上手可能需要摸清一下用法</p>
<h4 data-id="heading-9">4.server服务项目重点</h4>
<p>简单说说server文件(服务)的项目</p>
<h5 data-id="heading-10">运行</h5>
<ul>
<li><code>yarn install</code>: 安装依赖</li>
<li><code>yarn serve</code>: 运行项目</li>
</ul>
<h5 data-id="heading-11">自定义 mock 口访问(用于项目开发前端模拟接口使用)</h5>
<p>本地项目运行成功后，接口访问格式为 本地 ip 或者<code>localhost</code>+ 端口(统一为 6868)+ 所属模块的接口前缀(pathName)+ 所访问接口的接口地址(url)</p>
<p>例如，访问接口前缀为 user 的模块 下的 add 接口，访问地址如下：</p>
<pre><code class="hljs language-. copyable" lang=".">http://localhost:6868/user/add
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-12">UI 界面操作接口(用于 UI 界面操作)</h5>
<p>相关接口可见接口文档.md 文件，接口访问格式为 本地 ip 或者<code>localhost</code>+ 端口(统一为 6868)+ 接口名称(如‘/section/createSection’)</p>
<p>例如，访问创建模块接口，访问地址如下：</p>
<pre><code class="hljs language-. copyable" lang=".">http://localhost:6868/section/createSection
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">主要目录结构说明</h5>
<pre><code class="hljs language-. copyable" lang=".">├── public                --存放接口生成的静态数据
├── README.md             --项目说明文件
├── 接口文档.md             --接口说明文件
├── 接口测试用例.md         --接口测试用例说明文件
├── index.ts              --服务启动文件
├── logger.ts             --日志处理文件
├── server.ts             --服务主要处理文件
├── src                   --项目代码目录
├──── api                 --路由相关处理目录
├──── config               --环境配置目录
├──── controller          --接口参数校验目录
├──── enum                --常量目录
├──── service             --接口具体操作处理目录
├──── types               --相关参数的 interface 定义 目录
├──── utils               --工具方法目录
├──── validate            --接口参数校验方法目录
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">5.主要实现逻辑</h4>
<h5 data-id="heading-15">模块相关接口实现</h5>
<ol>
<li><strong>新增模块</strong>： public/sectionList 下新建以 pathName 命名的 json 文件（以下简称“模块 json 文件”），写入提交的模块相关信息；同时 public/下新建以 pathName 命名的文件夹（以下简称“模块接口文件夹”），用以存放该模块下的接口；</li>
<li><strong>修改模块</strong>： 修改模块 json 文件，对比旧的 pathName，如不一样，需要将模块 json 文件重命名以及模块接口文件夹以新的 pathName 重命名；</li>
<li><strong>获取模块详情</strong>： 找到模块 json 文件，读取文件内容；</li>
<li><strong>删除模块</strong>：删除模块 json 文件和模块接口文件夹(文件夹下的所有文件也需删除)；</li>
<li><strong>获取带分页的模块列表</strong>：获取 public/sectionList 文件夹下的所有 json 文件个数及内容，拼接为带 list 和 total 的对象返回。</li>
</ol>
<h5 data-id="heading-16">接口相关接口实现</h5>
<ol>
<li><strong>新增接口</strong>：根据 pathName 找到对应的模块接口文件夹，创建以 url 命名的 json 文件（以下简称“接口 json 文件”），写入提交的接口相关信息；</li>
<li><strong>修改接口</strong>：修改接口 json 文件，对比旧的 url，如不一样，需要将接口 json 文件以新的 url 重命名；</li>
<li><strong>获取接口详情</strong>： 找到接口 json 文件，读取文件内容；</li>
<li><strong>删除接口</strong>：删除接口 json 文件；</li>
<li><strong>获取带分页的接口列表</strong>：获取 模块接口文件夹下的所有 json 文件个数及内容，拼接为带 list 和 total 的对象返回。</li>
</ol>
<h5 data-id="heading-17">自定义 mock 接口实现</h5>
<p>  读取接口 json 文件数据，获取请求参数和响应内容参数。第一步，校验请求的必填参数是否有提交，其次校验提交的参数类型是否正确。第二步，在第一步成功的基础上，对响应内容的数据进行处理，处理为 mock 可接收的对象，然后通过 mock，模拟数据返回。</p>
<h4 data-id="heading-18">6.serve接口文档</h4>
<p>server的几个接口是重点 比如增加模块 增加接口删除接口等等 所以放出一些接口文档</p>
<p>(1) 接口返回成功示例</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  success: <span class="hljs-literal">true</span>  <span class="hljs-comment">// 主要通过这个字段去判断成功或者失败</span>
  message: <span class="hljs-string">"新增成功"</span>
  data: &#123;list: [,…], total: <span class="hljs-number">2</span>&#125;
  code: <span class="hljs-number">200</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>(2) 接口返回失败示例</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  success: <span class="hljs-literal">false</span>
  data: <span class="hljs-literal">null</span>
  message: <span class="hljs-string">"child "</span>url<span class="hljs-string">" fails because ["</span>url<span class="hljs-string">" is required]"</span>
  code: <span class="hljs-number">400</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>新增模块接口 post 方式 /section/createSection</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"模块1"</span>, <span class="hljs-comment">// 模块名称-必填</span>
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 创建的文件夹名称以及调用接口需要加的前缀-必填且只能是英文(页面就叫接口前缀吧),每个模块的pathName唯一</span>
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"模块介绍"</span> <span class="hljs-comment">// 接口描述可选</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>详情模块接口 post 方式 /section/getSectionDetail</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span> <span class="hljs-comment">// pathName-必填</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>更新模块接口 post 方式 /section/updateSection</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"id"</span>: <span class="hljs-number">123</span>, <span class="hljs-comment">// id-必填</span>
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"模块1"</span>, <span class="hljs-comment">// 模块名称-必填</span>
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 必填</span>
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"模块介绍"</span> <span class="hljs-comment">// 接口描述可选</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="4">
<li>删除模块接口 post 方式 /section/deleteSection</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span> <span class="hljs-comment">// pathName-必填</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="5">
<li>获取模块列表 post 方式 /section/getSectionList</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"page"</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 当前页数可选</span>
  <span class="hljs-attr">"size"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 每页显示条数可选</span>
  <span class="hljs-attr">"isPage"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 必填，表示是否分页，true分页、false不分页</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="6">
<li>新增接口 post 方式 /interface/createData</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-comment">// 提交参数</span>
&#123;
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 所属模块的模块pathName必填</span>
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"示例接口"</span>, <span class="hljs-comment">// 接口名必填</span>
  <span class="hljs-attr">"url"</span>: <span class="hljs-string">"/createJson"</span>, <span class="hljs-comment">// 接口地址必填</span>
  <span class="hljs-attr">"method"</span>: <span class="hljs-string">"GET"</span>, <span class="hljs-comment">// 接口请求方式可选，默认"POST"</span>
  <span class="hljs-attr">"status"</span>: <span class="hljs-number">200</span>, <span class="hljs-comment">// 状态码可选，默认200</span>
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"描述"</span> <span class="hljs-comment">// 接口描述可选</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>详情接口 post 方式 /interface/getDetailData</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 所属模块的模块pathName必填</span>
  <span class="hljs-attr">"url"</span>: <span class="hljs-string">"/createJson"</span> <span class="hljs-comment">// 接口地址必填</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="8">
<li>修改接口 post 方式 /interface/updateData （参数必填项还未全部确定）</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 所属模块的pathName必填</span>
  <span class="hljs-attr">"id"</span>: <span class="hljs-number">123</span>, <span class="hljs-comment">// 所更改的接口id--必填</span>
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"示例接口"</span>, <span class="hljs-comment">// 接口名--必填</span>
  <span class="hljs-attr">"url"</span>: <span class="hljs-string">"/createJson"</span>, <span class="hljs-comment">// 接口地址--必填</span>
  <span class="hljs-attr">"method"</span>: <span class="hljs-string">"GET"</span>, <span class="hljs-comment">// 接口请求方式--必填</span>
  <span class="hljs-attr">"status"</span>: <span class="hljs-number">200</span>, <span class="hljs-comment">// 状态码--必填</span>
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"描述"</span> <span class="hljs-comment">// 接口描述</span>
  <span class="hljs-comment">// 自定义请求参数</span>
  <span class="hljs-string">"request"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-number">100</span>,
        <span class="hljs-attr">"parentId"</span>: <span class="hljs-number">-1</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"name"</span>, <span class="hljs-comment">// 字段名</span>
        <span class="hljs-attr">"required"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否为必填项</span>
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"String"</span>, <span class="hljs-comment">// 字段类型</span>
        <span class="hljs-attr">"rule"</span>: <span class="hljs-string">""</span>, <span class="hljs-comment">// 生成规则</span>
        <span class="hljs-attr">"value"</span>: <span class="hljs-string">""</span>, <span class="hljs-comment">// 初始值</span>
        <span class="hljs-attr">"description"</span>: <span class="hljs-string">"数组属性示例"</span> <span class="hljs-comment">// 字段描述</span>
      &#125;,
    ],
  <span class="hljs-comment">// 自定义返回内容</span>
    <span class="hljs-attr">"response"</span>: [
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-number">6</span>,
        <span class="hljs-attr">"parentId"</span>: <span class="hljs-number">-1</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"数组"</span>, <span class="hljs-comment">// 字段名</span>
        <span class="hljs-attr">"required"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否为必填项</span>
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Array"</span>, <span class="hljs-comment">// 字段类型</span>
        <span class="hljs-attr">"rule"</span>: <span class="hljs-string">"1-2"</span>, <span class="hljs-comment">// 生成规则</span>
        <span class="hljs-attr">"value"</span>: <span class="hljs-string">""</span>, <span class="hljs-comment">// 初始值</span>
        <span class="hljs-attr">"description"</span>: <span class="hljs-string">"数组属性示例"</span> <span class="hljs-comment">// 字段描述</span>
      &#125;,
      &#123;
        <span class="hljs-attr">"id"</span>: <span class="hljs-number">11</span>,
        <span class="hljs-attr">"parentId"</span>: <span class="hljs-number">6</span>,
        <span class="hljs-attr">"name"</span>: <span class="hljs-string">"子元素1"</span>, <span class="hljs-comment">// 字段名</span>
        <span class="hljs-attr">"required"</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 是否为必填项</span>
        <span class="hljs-attr">"type"</span>: <span class="hljs-string">"Array"</span>, <span class="hljs-comment">// 字段类型</span>
        <span class="hljs-attr">"rule"</span>: <span class="hljs-string">"1-2"</span>, <span class="hljs-comment">// 生成规则</span>
        <span class="hljs-attr">"value"</span>: <span class="hljs-string">"@cname"</span>, <span class="hljs-comment">// 初始值</span>
        <span class="hljs-attr">"description"</span>: <span class="hljs-string">"数组一级子元素"</span> <span class="hljs-comment">// 字段描述</span>
      &#125;,
    ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li>删除接口 post 方式 /interface/deleteData</li>
</ol>
<pre><code class="hljs language-json copyable" lang="json">&#123;
   <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>, <span class="hljs-comment">// 所属模块的模块pathName必填</span>
   <span class="hljs-attr">"url"</span>: <span class="hljs-string">"/createJson"</span> <span class="hljs-comment">// 接口地址必填</span>
&#125;

<span class="hljs-number">10.</span> 获取接口列表，带分页 post 方式 /interface/getDataList

```json
&#123;
   <span class="hljs-attr">"pathName"</span>: <span class="hljs-string">"user"</span>,
  <span class="hljs-attr">"page"</span>: <span class="hljs-number">1</span>, <span class="hljs-comment">// 当前页数</span>
  <span class="hljs-attr">"size"</span>: <span class="hljs-number">2</span>, <span class="hljs-comment">// 每页显示条数</span>
  <span class="hljs-attr">"isPage"</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 必填，表示是否分页，true分页、false不分页</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">小结</h3>
<p>不同平台的mock服务有不同的优缺点，当然如果我的文章对你有帮助 我也是很开心的
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/492fe7462d1a434aa81512924e0f0c20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
选最适合你的 或者 最容易上手的 反正就是结合你自己的需求去选择。这里推荐<a href="https://yapi.baidu.com/doc/documents/index.html" target="_blank" rel="nofollow noopener noreferrer">YApi</a>。简单上手，尽量减少学习成本。Yapi这点比较好。简单的使用甚至不需要了解mock.js的api.直接配置即可。开源程度社区活跃度较高，且保持bug的修复与功能完善.</p>
<h3 data-id="heading-20">参考链接</h3>
<ol>
<li><a href="http://mockjs.com/0.1/#" target="_blank" rel="nofollow noopener noreferrer">mock官方文档</a> 和 <a href="https://github.com/nuysoft/Mock" target="_blank" rel="nofollow noopener noreferrer">项目地址</a></li>
<li><a href="https://yapi.baidu.com/doc/documents/index.html" target="_blank" rel="nofollow noopener noreferrer">yapi官方文档</a> 和  <a href="https://github.com/ymfe/yapi" target="_blank" rel="nofollow noopener noreferrer">项目地址</a></li>
<li><a href="https://blog.csdn.net/u014340331/article/details/105093557" target="_blank" rel="nofollow noopener noreferrer">常见MOCK-SERVER对比</a></li>
<li><a href="https://www.jianshu.com/p/15ebd51ea733" target="_blank" rel="nofollow noopener noreferrer">几个mock平台的个人感受</a></li>
<li><a href="https://www.cnblogs.com/bodhitree/p/9456515.html" target="_blank" rel="nofollow noopener noreferrer">Mockito 简明教程</a></li>
</ol>
<p><code>PS:别问我为什么把好链接放后面(放前面 你们还能看完我的文章嘛) 要是觉得不错，点个赞哦</code></p>
<h3 data-id="heading-21">结束语</h3>
<p>其实最近一直在练习 怎么取分享知识和写好文章。这两点我现在都做的不怎么好 也许是掌握不深 所以不知道怎样去表达知识点和分享精彩吸引人的内容。
如果能坚持写博客 记录一下自己使用的技术之类 对我来说也是一种进步 孰能生巧！</p>
<p><strong>点关注不迷路！你那么帅(漂亮)，都看到这了，动手点个赞鼓励一下作者吧，谢谢！</strong></p>
<p><code>点赞，点赞，点赞！ 非常谢谢！</code></p></div>  
</div>
            