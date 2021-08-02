
---
title: 'Flutter 封装：富文本 RichText 极简封装'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3d5f5ecf9354d9aa136980869fc776c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 21:08:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3d5f5ecf9354d9aa136980869fc776c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">1. 需求：</h4>
<p>开发中遇到一个富文本展示点击效果（用户协议和隐私），通过官方的原始方法能够实现，但是很繁琐而且无聊，随想实现一个方便且高效的富文本生成方法，参考 iOS，最终完美实现；</p>
<h4 data-id="heading-1">2. 实现原理：</h4>
<ol>
<li>
<p>声明协议字典, 例如</p>
<pre><code class="copyable">var linkMap = &#123;
  '《用户协议》': 'https://flutter.dev',
  '《隐私政策》': 'https://flutter.dev',
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>通过 《 》分割整段文字为数组；然后判断数组元素是否等于 “《$e》”; 如果等于则创建为链接 TextSpan），不等于则创建普通 TextSpan；可以得到 TextSpan 数组；</p>
</li>
<li>
<p>ontap 回调（点击链接）返回 linkMap 中对应 key 和 value；</p>
</li>
</ol>
<h4 data-id="heading-2">3. sceenshot:</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3d5f5ecf9354d9aa136980869fc776c~tplv-k3u1fbpfcp-watermark.image" alt="Simulator Screen Shot - iPhone 11 Pro - 2021-07-31 at 12.50.12.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">4. example:</h4>
<pre><code class="copyable">//
//  RichTextDemo.dart
//  fluttertemplet
//
//  Created by shang on 7/31/21 12:11 PM.
//  Copyright © 7/31/21 shang. All rights reserved.
//

import 'package:flutter/material.dart';
import 'package:fluttertemplet/basicWidget/AttributedString.dart';
import 'package:fluttertemplet/dartExpand/ddlog.dart';

class RichTextDemo extends StatefulWidget &#123;

  final String? title;

  RichTextDemo(&#123; Key? key, this.title&#125;) : super(key: key);


  @override
  _RichTextDemoState createState() => _RichTextDemoState();
&#125;

class _RichTextDemoState extends State<RichTextDemo> &#123;

  @override
  Widget build(BuildContext context) &#123;
    dynamic arguments = ModalRoute.of(context)!.settings.arguments;

    return Scaffold(
        appBar: AppBar(
          title: Text(widget.title ?? "$widget"),
        ),
        body: buildRichText(context),
    );
  &#125;

  Widget buildRichText(BuildContext context) &#123;

    var linkMap = &#123;
      '《用户协议》': 'https://flutter.dev',
      '《隐私政策》': 'https://flutter.dev',
    &#125;;

    String text = """
        亲爱的xxxx用户，感谢您信任并使用xxxxAPP！
xxxx十分重视用户权利及隐私政策并严格按照相关法律法规的要求，对《用户协议》和《隐私政策》进行了更新,特向您说明如下：
        1.为向您提供更优质的服务，我们会收集、使用必要的信息，并会采取业界先进的安全措施保护您的信息安全；
        2.基于您的明示授权，我们可能会获取设备号信息、包括：设备型号、操作系统版本、设备设置、设备标识符、MAC（媒体访问控制）地址、IMEI（移动设备国际身份码）、广告标识符（“IDFA”与“IDFV”）、集成电路卡识别码（“ICCD”）、软件安装列表。我们将使用三方产品（友盟、极光等）统计使用我们产品的设备数量并进行设备机型数据分析与设备适配性分析。（以保障您的账号与交易安全），且您有权拒绝或取消授权；
        3.您可灵活设置伴伴账号的功能内容和互动权限，您可在《隐私政策》中了解到权限的详细应用说明；
        4.未经您同意，我们不会从第三方获取、共享或向其提供您的信息；
        5.您可以查询、更正、删除您的个人信息，我们也提供账户注销的渠道。
        请您仔细阅读并充分理解相关条款，其中重点条款已为您黑体加粗标识，方便您了解自己的权利。如您点击“同意”，即表示您已仔细阅读并同意本《用户协议》及《隐私政策》，将尽全力保障您的合法权益并继续为您提供优质的产品和服务。如您点击“不同意”，将可能导致您无法继续使用我们的产品和服务。
""";
    final textRich = Text.rich(
      TextSpan(
        children: AttributedString(
            context: context,
            text: text,
            linkMap: linkMap,
            // style: TextStyle(
            //     fontSize: 13,
            // ),
            // linkStyle: TextStyle(fontSize: 15),
            onTap: (key, value)&#123;
              ddlog(key);
              ddlog(value);
            &#125;
        ).textSpans,
      ),
      strutStyle: StrutStyle(
        leading: 0.4,
      ),
    );

    return Container(
      padding: EdgeInsets.all(12),
      child: textRich,
    );
  &#125;
&#125;

//flutter: 2021-07-31 12:57:28.257309  RichTextDemo.dart, _RichTextDemoState [line 66]: 《用户协议》
//flutter: 2021-07-31 12:57:28.257929  RichTextDemo.dart, _RichTextDemoState [line 67]: https://flutter.dev
//flutter: 2021-07-31 12:57:28.890716  RichTextDemo.dart, _RichTextDemoState [line 66]: 《隐私政策》
//flutter: 2021-07-31 12:57:28.891331  RichTextDemo.dart, _RichTextDemoState [line 67]: https://flutter.dev
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">5. 两种封装方式：</h4>
<p>扩展封装:
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshang1219178163%2Ffluttertemplet%2Fblob%2Fdevelop%2Flib%2FdartExpand%2FrichText_extension.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shang1219178163/fluttertemplet/blob/develop/lib/dartExpand/richText_extension.dart" ref="nofollow noopener noreferrer">richText_extension.dart</a></p>
<pre><code class="copyable">//...
children: RichTextExt.createTextSpans(context,
    text: text,
    linkMap: protocolMap,
    onTap: (key, value)&#123;
      ddlog(key);
      ddlog(value);
    &#125;
)
//...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类封装:
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshang1219178163%2Ffluttertemplet%2Fblob%2Fdevelop%2Flib%2FbasicWidget%2FAttributedString.dart" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shang1219178163/fluttertemplet/blob/develop/lib/basicWidget/AttributedString.dart" ref="nofollow noopener noreferrer">AttributedString.dart</a></p>
<pre><code class="copyable">//...
// children: AttributedString(
//     context: context,
//     text: text,
//     linkMap: protocolMap,
//     onTap: (key, value)&#123;
//       ddlog(key);
//       ddlog(value);
//     &#125;
// ).textSpans,
//...
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            