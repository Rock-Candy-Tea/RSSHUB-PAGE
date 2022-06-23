
---
title: '集成 2.6 万亿个 7nm 晶体管，世界最大 AI 芯片打破单设备训练大模型记录'
categories: 
 - 新媒体
 - IT 之家
 - 分类资讯
headimg: 'https://img.ithome.com/newsuploadfiles/2022/6/fcd23e23-8b7a-4d02-ad54-04418dbcc8d3.jpg'
author: IT 之家
comments: false
date: Thu, 23 Jun 2022 11:32:52 GMT
thumbnail: 'https://img.ithome.com/newsuploadfiles/2022/6/fcd23e23-8b7a-4d02-ad54-04418dbcc8d3.jpg'
---

<div>   
<p data-vmark="8ecb">以造出世界上最大加速器芯片 CS-2 Wafer Scale Engine 闻名的公司 Cerebras 昨日宣布他们已经在利用“巨芯”进行人工智能训练上走出了重要的一步。<strong>该公司训练出了单芯片上全世界最大的 NLP（自然语言处理）AI 模型</strong>。</p><p data-vmark="208a">该模型具有 20 亿个参数，基于 CS-2 芯片进行训练。这块全世界最大的加速器芯片采用 7nm 制程工艺，由一整块方形的晶圆刻蚀而成。它的大小数百倍于主流芯片，具有 15KW 的功率。<strong>它集成了 2.6 万亿个 7nm 晶体管，封装了 850000 个内核和 40GB 内存</strong>。</p><p data-vmark="de63" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/6/fcd23e23-8b7a-4d02-ad54-04418dbcc8d3.jpg" w="740" h="384" alt="世界最大AI芯片打破单设备训练大模型记录 ，Cerebras要「杀死」GPU " title="集成 2.6 万亿个 7nm 晶体管，世界最大 AI 芯片打破单设备训练大模型记录" width="740" height="384" referrerpolicy="no-referrer"></p><p style="text-align: center;" data-vmark="ab6c">▲ 图 1 CS-2 Wafer Scale Engine 芯片</p><h2 data-vmark="4b27">单芯片训练 AI 大模型新纪录</h2><p data-vmark="2cee">NLP 模型的开发是人工智能中的一个重要领域。利用 NLP 模型，人工智能可以“理解”文字含义，并进行相应的动作。OpenAI 的 DALL.E 模型就是一个典型的 NLP 模型。<strong>这个模型可以将使用者的输入的文字信息转化为图片输出</strong>。</p><p data-vmark="0030">比如当使用者输入“牛油果形状的扶手椅”后，AI 就会自动生成若干与这句话对应的图像。</p><p data-vmark="5506" style="text-align: center;"><img src="https://img.ithome.com/newsuploadfiles/2022/6/7e3329f4-c04c-4915-b92f-3b2de098d0d4.jpg" w="740" h="361" alt="世界最大AI芯片打破单设备训练大模型记录 ，Cerebras要「杀死」GPU " title="集成 2.6 万亿个 7nm 晶体管，世界最大 AI 芯片打破单设备训练大模型记录" width="740" height="361" referrerpolicy="no-referrer"></p><p style="text-align: center;" data-vmark="abb6">▲ 图：AI 接收信息后生成的“牛油果形状扶手椅”图片</p><p data-vmark="35d9">不止于此，该模型还能够使 AI 理解物种、几何、历史时代等复杂的知识。</p><p data-vmark="2ad4">但要实现这一切并不容易，NLP 模型的传统开发具有极高的算力成本和技术门槛。</p><p data-vmark="8967">实际上，如果只讨论数字，Cerebras 开发的这一模型 20 亿的参数量在同行的衬托下，显得有些平平无奇。</p><p data-vmark="53fc">前面提到的 DALL.E 模型具有 120 亿个参数，而目前最大的模型是 DeepMind 于去年年底推出的 Gopher，<strong>具有 2800 亿个参数</strong>。</p><p data-vmark="778c">但除去惊人的数字外，Cerebras 开发的 NLP 还有一个巨大的突破：它降低了 NLP 模型的开发难度。</p><h2 data-vmark="f7c8">「巨芯」如何打败 GPU？</h2><p data-vmark="4e7c">按照传统流程，开发 NLP 模型需要开发者将巨大的 NLP 模型切分若干个功能部分，并将他们的工作负载分散到成百上千个图形处理单元上。</p><p data-vmark="2a81">数以千百计的图形处理单元对厂商来说意味着巨大的成本。</p><p data-vmark="d9ab">技术上的困难也同样使厂商们痛苦不堪。</p><p data-vmark="3d6d">切分模型是一个定制的问题，<strong>每个神经网络、每个 GPU 的规格、以及将他们连接（或互联）在一起的网络都是独一无二的</strong>，并且不能跨系统移植。</p><p data-vmark="207a">厂商必须在第一次训练前将这些因素统统考虑清楚。</p><p data-vmark="22d1">这项工作极其复杂，有时候甚至需要几个月的时间才能完成。</p><p data-vmark="554b">Cerebras 表示这是 NLP 模型训练中“最痛苦的方面之一”。只有极少数公司拥有开发 NLP 所必要的资源和专业知识。对于人工智能行业中的其他公司而言，NLP 的训练则太昂贵、太耗时且无法使用。</p><p data-vmark="6908">但如果单个芯片就能够支持 20 亿个参数的模型，就意味着不需要使用海量的 GPU 分散训练模型的工作量。这可以为厂商节省数千个 GPU 的训练成本和相关的硬件、扩展要求。同时这也使厂商不必经历切分模型并将其工作负载分配给数千个 GPU 的痛苦。</p><p data-vmark="d9cd">Cerebras 也并未仅仅执拗于数字，评价一个模型的好坏，参数的数量并不是唯一标准。</p><p data-vmark="153f">比起希望诞生于“巨芯”上的模型“努力”，Cerebras 更希望的是模型“聪明”。</p><p data-vmark="5c53">之所以 Cerebras 能够在参数量上取得爆炸式增长，是因为利用了权重流技术。这项技术可以将计算和内存的占用量解耦，并允许将内存扩展到足以存储 AI 工作负载中增加的任何数量的参数。</p><p data-vmark="7a8b">由于这项突破，设置模型的时间从几个月减少到了几分钟。并且开发者在 GPT-J 和 GPT-Neo 等型号之间“只需几次按键”就可以完成切换。这让 NLP 的开发变得更加简单。</p><p data-vmark="83c6">这使得 NLP 领域出现了新的变化。</p><p data-vmark="bb70">正如 Intersect360 Research 首席研究官 Dan Olds 对 Cerebras 取得成就的评价：“Cerebras 能够以具有成本效益、易于访问的方式将大型语言模型带给大众，这为人工智能开辟了一个激动人心的新时代。”</p>
          
</div>
            