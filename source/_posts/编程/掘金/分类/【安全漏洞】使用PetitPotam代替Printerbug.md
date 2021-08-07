
---
title: '【安全漏洞】使用PetitPotam代替Printerbug'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48beaf01d5f4405aa94e90391d85c8c5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 22:51:16 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48beaf01d5f4405aa94e90391d85c8c5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0"><strong>前言</strong></h1>
<p>Printerbug使得拥有控制域用户/计算机的攻击者可以指定域内的一台服务器，并使其对攻击者选择的目标进行身份验证。虽然不是一个微软承认的漏洞，但是跟Net-ntlmV1,非约束委派，NTLM_Relay,命名管道模拟这些手法的结合可以用来域内提权，本地提权，跨域等等利用。</p>
<p>遗憾的是，在PrintNightmare爆发之后，很多企业会选择关闭spoolss服务，使得Printerbug失效。在Printerbug逐渐失效的今天，PetitPotam来了，他也可以指定域内的一台服务器，并使其对攻击者选择的目标进行身份验证。而且在低版本(16以下)的情况底下，可以匿名触发。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48beaf01d5f4405aa94e90391d85c8c5~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77f490d4b5e247648f46a46f8e3af5fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<h1 data-id="heading-1"><strong>原理</strong></h1>
<p>MS-EFSR里面有个函数EfsRpcOpenFileRaw(Opnum 0)</p>
<pre><code class="copyable">long EfsRpcOpenFileRaw(
   [in] handle_t binding_h,
   [out] PEXIMPORT_CONTEXT_HANDLE* hContext,
   [in, string] wchar_t* FileName,
   [in] long Flags
 );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>他的作用是打开服务器上的加密对象以进行备份或还原，服务器上的加密对象由FileName 参数指定,FileName的类型是UncPath。</p>
<p>当指定格式为\IP\C$的时候，lsass.exe服务就会去访问\IP\pipe\srvsrv</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72bebc5fcf574a12ba7c54c89c90acb8~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ecb4b64562474251920e4b363116763d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>指定域内的一台服务器，并使其对攻击者选择的目标(通过修改FileName里面的IP参数)进行身份验证。</p>
<p> </p>
<h1 data-id="heading-2"><strong>细节</strong></h1>
<p><strong>1、通过lsarpc 触发</strong></p>
<p>在<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fdocs.microsoft.com%252Fen-us%252Fopenspecs%252Fwindows_protocols%252Fms-efsr%252F403c7ae0-1a3a-4e96-8efc-54e79a2cc451" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.microsoft.com%2Fen-us%2Fopenspecs%2Fwindows_protocols%2Fms-efsr%2F403c7ae0-1a3a-4e96-8efc-54e79a2cc451" ref="nofollow noopener noreferrer">官方文档</a>里面，MS-EFSR的调用有\pipe\lsarpc和\pipe\efsrpc两种方法，其中</p>
<p><strong>·</strong>  \pipe\lsarpc的服务器接口必须是UUID [c681d488-d850-11d0-8c52-00c04fd90f7e]</p>
<p><strong>·</strong>  \pipe\efsrpc的服务器接口必须是UUID [df1941c5-fe89-4e79-bf10-463657acf44d]</p>
<p>在我本地测试发现\pipe\efsrpc并未对外开放</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/833422d8f4824a54b7754085c85ef2dc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f4146d21296749248cd742223a80a7fb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在PetitPotam的Poc里面有一句注释possible aussi via efsrpc (en changeant d'UUID) mais ce named pipe est moins universel et plus rare que lsarpc ;)，翻译过来就是</p>
<p>也可以通过EFSRPC（通过更改UUID），但这种命名管道的通用性不如lsarpc，而且比LSARPC更罕见</p>
<p>所以PetitPotam直接是采用lsarpc的方式触发。</p>
<p><strong>2、低版本可以匿名触发</strong></p>
<p>在08和12的环境，默认在网络安全:可匿名访问的命名管道中有三个netlogon、samr、lsarpc。因此在这个环境下是可以匿名触发的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d19e21e55ab4762869b744f5b7e2fdc~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66e73ce5c28d467f8fe5187295889a9e~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf36c8bb6d614dd799569deb2236e37e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a49ee8c6d25143fb9f63acf54743180e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>遗憾的是在16以上这个默认就是空了，需要至少一个域内凭据。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/378b28a23b6d47aeb7dae66cc652d034~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<h1 data-id="heading-3"><strong>利用</strong></h1>
<p>这篇文章的主题是使用PetitPotam代替Printerbug，因此这个利用同时也是Printerbug的利用。这里顺便梳理复习下Printerbug的利用。</p>
<p><strong>1、结合 CVE-2019-1040，NTLM_Relay到LDAP</strong></p>
<p>详情见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fdaiker.gitbook.io%252Fwindows-protocol%252Fntlm-pian%252F7%25235-cve-2019-1040" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdaiker.gitbook.io%2Fwindows-protocol%2Fntlm-pian%2F7%235-cve-2019-1040" ref="nofollow noopener noreferrer">CVE-2019-1040</a>,这里我们可以将触发源从Printerbug换成PetitPotam</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cb2bcbcb3d54b3d8bba7c65ac61187a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f17708afc4548f4a2ecca3530d440b7~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><strong>2、Relay到HTTP</strong></p>
<p>不同于LDAP是协商签名的，发起的协议如果是smb就需要修改Flag位，到HTTP的NTLM认证是不签名的。前段时间比较火的ADCS刚好是http接口，又接受ntlm认证，我们可以利用PetitPotam把域控机器用户relay到ADCS里面申请一个域控证书，再用这个证书进行kerberos认证。注意这里如果是域控要指定模板为DomainController</p>
<pre><code class="copyable">python3 ntlmrelayx.py -t https://192.168.12.201/Certsrv/certfnsh.asp -smb2support --adcs --template "DomainController"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa65a6dbc9c4502bad4e7fb742b1f2d~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd66f602999a4f0f9f310abe04fb51f5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>2、结合非约束委派的利用</strong></p>
<p>当一台机器机配置了非约束委派之后，任何用户通过网络认证访问这台主机，配置的非约束委派的机器都能拿到这个用户的TGT票据。</p>
<p>当我们拿到了一台非约束委派的机器，只要诱导别人来访问这台机器就可以拿到那个用户的TGT，在这之前我们一般用printerbug来触发，在这里我们可以用PetitPotamlai来触发。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/517ad55146b94507b6c4f67eea5afc40~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a32faf717c394a9fb218fa21c4d89c1a~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b279a85c301942cfa035bed712b8780b~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7060bdb4d42a4359b43819a130e929f0~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>域内默认所有域控都是非约束委派，因此这种利用还可用于跨域。</p>
<p><strong>3、结合Net-ntlmV1进行利用</strong></p>
<p>很多企业由于历史原因，会导致LAN身份验证级别配置不当，攻击者可以将Net-Ntlm降级为V1</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82dc1b6c2fb14c2da0329ae90957c03b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c7faa6624374de38f25886a8b7923c5~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们在Responder里面把Challeng设置为1122334455667788,就可以将Net-ntlm V1解密为ntlm hash</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1bced3fb59064fc5bf4fa22a5cfeb32a~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43b038cc9ab34c3880ab1c947fd9088d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d8bdf03398e4aa6b6ef9a1c1a3e9cb7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f6998e5ad3c54b4b88ea1d266f2f9c4c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>4、结合命名管道的模拟</strong></p>
<p>在这之前，我们利用了printerbug放出了pipePotato漏洞。详情见<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.oschina.net%2Faction%2FGoToLink%3Furl%3Dhttps%253A%252F%252Fwww.anquanke.com%252Fpost%252Fid%252F204510" target="_blank" rel="nofollow noopener noreferrer" title="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.anquanke.com%2Fpost%2Fid%2F204510" ref="nofollow noopener noreferrer">pipePotato：一种新型的通用提权漏洞</a>。</p>
<p>在PetitPotam出来的时候，发现这个RPC也会有之前pipePotato的问题。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/921e0a0591114f7d926132c70090ad77~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3fbfd6283ce417e92d82b9a3d64f0b5~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f0ff3c608304ca1a7642b983459ffaf~tplv-k3u1fbpfcp-watermark.image" alt="使用PetitPotam代替Printerbug" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bbcb3b8bb5d48dbb1e88ca07b87f7c4~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ebe3e742c4542018d10aa1cfff22eed~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<p>希望这篇文你看了后，能让你对网络安全的认知更加的广泛！！！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2d1526de6f840fd9cf54dda4e805e34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            