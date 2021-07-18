
---
title: '这一次，彻底搞懂React生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e141ab2d905c4b28835fc65b96138858~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 00:48:41 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e141ab2d905c4b28835fc65b96138858~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">阅读指南</h1>
<blockquote>
<p>本文采用总分总的结构，首先给出React生命周期流程图，让大家知道我们的研究目标是什么，第二部分则分别对React生命周期中的重点难点的生命钩子函数进行介绍。第三部分给出React生命周期的总结。</p>
</blockquote>
<h1 data-id="heading-1">React生命周期流程图</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e141ab2d905c4b28835fc65b96138858~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">1. getDerivedStateFromProps(props, state)</h2>
<blockquote>
<p>官方解释：调用这个钩子函数，会使得state在任何时候的状态值都取决于props.</p>
</blockquote>
<h3 data-id="heading-3">这个函数是静态的，所以前面要加static.</h3>
<h3 data-id="heading-4">返回的是什么？</h3>
<blockquote>
<p>返回的应该是状态对象（或者null）,总之返回的应该是一个对象，如果你什么都不返回，会出现警告。<strong>这个返回的对象就是render要渲染的state</strong></p>
</blockquote>
<h3 data-id="heading-5">接收的是什么？</h3>
<blockquote>
<p>接收两个参数，一个是最新的props，一个是最新的state.</p>
</blockquote>
<h3 data-id="heading-6"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freactzhonggetderivedstatefromprops-qzmmq%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/reactzhonggetderivedstatefromprops-qzmmq?file=/src/index.js" ref="nofollow noopener noreferrer">codeSandBox在线演示</a></h3>
<hr>
<h2 data-id="heading-7">2. shouldComponentUpdate(nextProps, nextState)</h2>
<h3 data-id="heading-8">接收的是什么？</h3>
<blockquote>
<p>接收两个参数，一个是最新的但是还未render的props，另一个则是最新的但是还未render的state.</p>
</blockquote>
<h3 data-id="heading-9">返回的是什么？</h3>
<blockquote>
<p>返回的是布尔值，返回true则让当前组件进行更新，返回false则让当前组件不更新。</p>
</blockquote>
<h3 data-id="heading-10"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freactzhongshouldcomponentupdatedeyongfa-9v08q%3Ffile%3D%2Fsrc%2Findex.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/reactzhongshouldcomponentupdatedeyongfa-9v08q?file=/src/index.js" ref="nofollow noopener noreferrer">codeSandBox在线演示</a></h3>
<hr>
<h2 data-id="heading-11">3. componentDidMount</h2>
<h3 data-id="heading-12">接受的是什么？</h3>
<blockquote>
<p>这个生命周期钩子函数是在挂载的最后阶段调用，并未接收参数。</p>
</blockquote>
<h3 data-id="heading-13">可以在这个钩子函数中处理组件挂载后的一些操作。</h3>
<h2 data-id="heading-14">4. getSnapshotBeforeUpdate(preProps,preState)</h2>
<h3 data-id="heading-15">接收的是什么？</h3>
<blockquote>
<p>接收两个参数，一个是之前的props，一个是之前的state.</p>
</blockquote>
<h3 data-id="heading-16">返回的是什么？</h3>
<blockquote>
<p>在这个生命周期钩子函数中，记录了更新DOM之前的一些HTML属性，返回的值，会被componentDidUpdate的第三个参数接收。</p>
</blockquote>
<h3 data-id="heading-17"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fgetsnapshotbeforeupdateyingyongxinwengundongtiaoanli-ryvlw" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/getsnapshotbeforeupdateyingyongxinwengundongtiaoanli-ryvlw" ref="nofollow noopener noreferrer">codeSandBox在线演示（新闻滚动条案例）</a></h3>
<h2 data-id="heading-18">5. componentDidUpdate(prevProps, prevState, snapshot)</h2>
<h3 data-id="heading-19">接收的是什么？</h3>
<blockquote>
<p>接收的是之前的props和之前的state，这个state是滞后与DOM的，同时第三个参数是接收的getSnapshotBeforeUpdate传来的参数。</p>
</blockquote>
<h3 data-id="heading-20">返回的是什么？</h3>
<blockquote>
<p>并不会返回什么，但是可以在此处进行更新后的对比，并对DOM进行操作，或者发起网络请求。</p>
</blockquote>
<h2 data-id="heading-21">6. componentWillUnmount()</h2>
<blockquote>
<p>该生命周期函数会在组件卸载之前调用，在这个方法中可以进行清除定时器等操作。在这个生命周期钩子函数中不应调用setState，因为如果这样组件将永远不会重新渲染。</p>
</blockquote>
<h2 data-id="heading-22">7. forceUpdate(callback)</h2>
<blockquote>
<p>该生命周期函数不用更改state或props也能对组件进行更新，调用render，且不用通过shouldComponentUpdate这个钩子。</p>
</blockquote>
<h3 data-id="heading-23"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Freactzhiforceupdatedeshiyong-nfb8r%3Ffile%3D%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/reactzhiforceupdatedeshiyong-nfb8r?file=/index.html" ref="nofollow noopener noreferrer">codeSandBox在线演示</a></h3>
<h2 data-id="heading-24">总结生命周期</h2>
<blockquote>
<p>React生命周期最关键的是要记住每一个生命周期钩子函数接收的是什么？返回的是什么？在什么阶段调用，这是核心也是关键，最后一定要熟记流程图！</p>
</blockquote></div>  
</div>
            