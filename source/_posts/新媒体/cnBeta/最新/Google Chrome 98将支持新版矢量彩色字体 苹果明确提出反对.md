
---
title: 'Google Chrome 98将支持新版矢量彩色字体 苹果明确提出反对'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0201/2628a86fb85afee.png'
author: cnBeta
comments: false
date: Tue, 01 Feb 2022 09:17:28 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0201/2628a86fb85afee.png'
---

<div>   
1月初，Google Chrome
97登陆稳定频道，带来了大量的新功能，包括更新的键盘API，该API被苹果和Mozilla驳回，因为它太容易侵犯用户隐私了。经过四周的开发周期，今<strong>天我们可以期待Chrome
98的发布，虽然它没有那么多的争议，但有一个功能“COLRv1”绝对是突出的，不仅如此它还引发了争议。</strong><br>
 <p><img src="https://static.cnbetacdn.com/article/2022/0201/2628a86fb85afee.png" title alt="image.png" referrerpolicy="no-referrer"></p><p>Google Chrome 98增加了对COLRv1彩色渐变矢量字体的支持，这是其COLRv0的进化版。 它们以渐变、合成、变换、多色字母的形式带来了更具表现力的视觉能力，甚至在非常小的字体尺寸下也是如此。Google对此介绍说，它能够使用COLRv1字体格式渲染诺托彩色表情符号，经过WOFF2压缩后的大小为1.85MB。同时，对于同样的表情符号，标准的位图字体占用了9MB，在节省系统资源开销上，这是个重大的改进。</p><p>与任何新的浏览器功能一样，获得其他网络浏览器供应商和网络开发者的支持以确保无缝的交叉兼容是非常重要的。尽管Mozilla和网络开发者已经提到他们对新的矢量字体的支持，但<a data-link="1" href="https://apple.pvxt.net/c/1251234/435400/7639?u=https%3A%2F%2Fwww.apple.com%2Fcn%2Fmusic%2F" target="_blank">苹果</a>的WebKit和Core Text团队则反对该提议，他们反对COLRv1的理由如下：</p><p>它重新发明了车轮。这种新的格式与任何通用的2D图形序列化格式一样，具有很强的表现力和功能。现有的通用2D图形的序列化格式有很多很多。</p><p>它还不存在于Chrome的开发者行列之外。OT-SVG同样具有表达能力，存在并在DirectWrite、Core Text、Firefox和许多（大部分）Adobe创作应用程序中拥有运输实现。许多OT-SVG字体已经存在。</p><p>因为这个建议在Chrome之外还不存在，所以在现有的创作工具中没有生态系统。相反，许多设计创作工具已经导出了SVG。</p><p>同时支持OT-SVG和这个新的提议是两倍（-ish）的维护负担，而这种格式并不比我们已经支持的格式更具表现力。</p><p>同时支持OT-SVG和这个新提议会增加我们的二进制大小。我们预计额外的二进制大小的增加大致相当于我们在实施 OT-SVG 后观察到的二进制大小的增加。(OT-SVG 涉及到一个 XML 解析器，但是 WebKit 已经与一个 XML 解析器关联，所以预计这个新提议的大小与我们在实现 OT-SVG 后看到的大小增加大致相等，而这个提议需要它自己的新型解析/溢出检测/解释代码）。</p><p>同时支持OT-SVG和这个新提议，使基于矢量的彩色字体的安全攻击的表面积增加了一倍。</p><p>即使考虑到一个只支持这个建议而不支持SVG的引擎，也没有看到任何证据表明，与一个新的二进制格式相比，避免使用XML会减少安全漏洞。历史上，在WebKit中，我们观察到不透明的二进制格式（如图像格式）有很多自己的安全漏洞。</p><p>这个规范有2500多行，规范的images/目录有77个数字，而这个建议只有一个实现。它足够复杂，以至于我们没有信心它能够被互操作地实现。我们担心绘图操作的行为可能是Skia特有的，而在Core Graphics上很难/不可能实现。例如，乍一看，我们不确定这个提案中的径向梯度是否可以在Core Graphics上实现。据我们所知，这个建议并没有经过许多独立的利益相关者的严格的标准化过程。</p><p>在彩色字体表格中嵌入光栅图像数据在今天是很常见的，但是这个新的提议没有允许这样做的能力，尽管它的矢量设施与任何通用的2D图形序列化格式一样具有表现力。因此，它实际上并没有改善彩色字体表碎片的情况，而这被广泛认为是当今彩色字体的最大缺点之一。</p><p>不过，不管苹果方面如何反对，COLRv1字体格式将首先在Chrome 98中得到支持。</p><p>除此以外，Chrome 98中还包括其他较小的改进和提高。用于密钥交换的简单数据加密标准（SDES）也正在被淘汰，因为它被称为"历史性的"，因此是一种安全风险。</p><p>一个CSS媒体查询也被提供给网页开发人员，以便他们能够自动检测HDR显示器并相应地渲染他们的内容。对于颜色调整，"only"关键字已被重新引入到CSS色彩模式规范中。</p><p>为了替代潜在的性能优势和对某些用例的简易开发，正在为"ClipboardItem"对象添加对承诺的支持。此外，开发者还可以利用"self.structuredClone()"方法来克隆和转移对象。为了避免混淆并实现与标准规范的互操作性，一些用于窗口弹出的API也被改变。</p><p>流写入现在可以立即被终止，跨源资源共享（CORS）预检请求也可以发送到私人网络上的目标服务器，在访问子资源之前首先明确询问权限。另一种方法使开发人员能够使用文件句柄更容易地删除文件，而不是被迫先访问父目录。</p><p><strong>了解有关COLRv1更多细节：</strong></p><p><a href="https://developer.chrome.com/blog/colrv1-fonts/" _src="https://developer.chrome.com/blog/colrv1-fonts/" target="_blank">https://developer.chrome.com/blog/colrv1-fonts/</a><br></p><p><strong>但这还不是全部，Chrome 98的DevTools中还有不少改进，您可以在这里查看所有的内容：</strong></p><p><a href="https://developer.chrome.com/blog/new-in-devtools-98/" _src="https://developer.chrome.com/blog/new-in-devtools-98/" target="_blank">https://developer.chrome.com/blog/new-in-devtools-98/</a><br></p><p>Chrome 98将在今天晚些时候开始推出。如果你在一天中没有自动更新到98版，请到帮助>关于Google Chrome，一旦有了更新，就可以触发它。接下来是Chrome 99，它将于2月3日进入Beta通道，并将于3月1日登陆稳定版。</p>   
</div>
            