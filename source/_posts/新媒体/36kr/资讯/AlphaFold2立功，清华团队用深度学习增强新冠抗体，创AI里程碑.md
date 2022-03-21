
---
title: 'AlphaFold2立功，清华团队用深度学习增强新冠抗体，创AI里程碑'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://img.36krcdn.com/20220321/v2_84baa776e90e47d09514650b288df72b_img_000'
author: 36kr
comments: false
date: Mon, 21 Mar 2022 05:01:06 GMT
thumbnail: 'https://img.36krcdn.com/20220321/v2_84baa776e90e47d09514650b288df72b_img_000'
---

<div>   
<blockquote> 
 <p>AlphaFold 2的问世可谓是生物学界海啸级地震，让蛋白质结构预测走上另一个新阶段。同时，AlphaFold的开创性方法也对其他研究产生深远的影响。这不，清华和MIT研究团队在最新研究中就用上了它。</p> 
</blockquote> 
<p>2020年末，DeepMind开发的第二代深度学习神经网络AlphaFold 2的问世震惊了结构生物学界。 </p> 
<p>AlphaFold解决了困扰科学家几十年的蛋白质折叠问题。 </p> 
<p class="image-wrapper"><img data-img-size-val="1024,576" src="https://img.36krcdn.com/20220321/v2_84baa776e90e47d09514650b288df72b_img_000" referrerpolicy="no-referrer"></p> 
<p>最近的研究表明，AlphaFold开创的方法正在向更广泛的生物学界蔓延。 </p> 
<p>在《美国国家科学院院刊》上发表的一篇论文 Deep learning guided optimization of human antibody against SARS-CoV-2 variants with broad neutralization。 </p> 
<p>论文中，科学家描述了修改一种已知的COVID-19抗体的方式，以提高其对多种疾病变体的疗效。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,323" src="https://img.36krcdn.com/20220321/v2_91b04feeb82b4a1c9321e97f4e3db398_img_000" referrerpolicy="no-referrer"></p> 
<p>地址：https://www.pnas.org/doi/10.1073/pnas.2122954119 </p> 
<p>科学家们写道，「我们可以使抗体宽度以及sars-cov-2变体 (包括 Delta) 的效力提高10到600倍」。他们甚至发现了该方法可以对抗奥密克戎（Omicron）变体迹象的希冀。 </p> 
<h2><strong>深度学习增强新冠抗体</strong></h2> 
<p>这项研究是由清华大学、<a class="project-link" data-id="25728" data-name="伊利" data-logo="https://img.36krcdn.com/20201021/v2_1ec775d2590347d8aa738b65409c4cbf_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/25728" target="_blank">伊利</a>诺伊大学厄巴纳-香槟分校和麻省理工学院的研究人员共同完成， 他们利用深度学习进行研究有两个重要的原因。 </p> 
<p>一个是扩大所谓的搜索空间，即修改抗体的一组潜在解决方案。现有的方法，例如随机突变，虽然很有价值，但费时费力。 </p> 
<p>使用深度学习是一种自动化的方法，从而加快工作速度。 </p> 
<p>其次，像随机突变这样的方法可以在带来好处的同时带走抗体好的那一部分，结果可能不是最理想的。 </p> 
<p>通过使用深度学习的方法，作者希望扩展功效的同时保留已经取得的成果。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,561" src="https://img.36krcdn.com/20220321/v2_6851c96423484d509e387de740e7d49f_img_000" referrerpolicy="no-referrer"></p> 
<p class="img-desc">图嵌入注意程序，用于查找对预测结合亲和力具有重要意义的残基对 </p> 
<p>他们的方法采用了AlphaFold2的基本技术: 一个图形网络，以及一种称为注意力机制的变量处理方法 </p> 
<p>图形网络是指一些事物的集合可以根据它们之间的关系进行评估，比如社交网络中的人。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,511" src="https://img.36krcdn.com/20220321/v2_4ee3923697a44ea4ae90071704cae31a_img_000" referrerpolicy="no-referrer"></p> 
<p>AlphaFold 2利用蛋白质的信息构建了一个不同氨基酸之间距离的图表。然后通过注意力机制操纵这些图，计算每个氨基酸与另一个氨基酸的关系。 </p> 
<p>Shan和他的同事采取了同样的方法，他们把这种方法应用到病毒的氨基酸、抗原以及抗体的氨基酸上。 </p> 
<p>他们将所谓的野生型与两者的突变形式进行比较，以确定抗体与抗原的结合如何随着野生型和突变型之间的氨基酸对的变化而变化。 </p> 
<p>为了训练一个深度神经网络实现这一点，他们设置了一个目标。在机器学习领域被称作目标函数，该函数正是神经网络要复制的目标。 </p> 
<p>在这一例中，目标函数是自由能量的变化，即蛋白质中的能量从野生型变到突变型，由希腊字母delta-delta、G和ΔΔG。 </p> 
<p>给定一个目标自由能，神经网络可以可靠地预测哪一组氨基酸配对的变化和目标自由能的变化最相符。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,599" src="https://img.36krcdn.com/20220321/v2_dc2e1596f46743a2a2fa810654b75a33_img_000" referrerpolicy="no-referrer"></p> 
<p>Shan和他的同事表示，为了评估变异对蛋白质复合体的效果，我们首先通过重新包装突变周围的侧链，预测了蛋白质复合体的结构，之后解码了野生型和突变型复合体，并利用该网络来获得野生型和突变型复合体的嵌入。 </p> 
<p>之后，通过额外的神经网络层和两部分嵌入的比较来预测突变的影响（用ΔΔG衡量）。 </p> 
<p>虽然Shan和他的团队提到了AlphaFold2，他们也使用了AlphaFold2所使用的方法，但他们没用DeepMind的代码。 </p> 
<p>麻省理工学院的Bonnie Berger是该研究的联合作者，他表示，「关于ΔΔG预测器的研究完全是从零开始的。」 </p> 
<p>因为ΔΔG预测器和AlphaFold2都是开源的，每个人都可以亲自去体验，去看看二者的比较。ΔΔG预测器的代码在GitHub，AlphaFold2的代码在它自己的网站。 </p> 
<p>在训练神经网络预测重要的抗体和抗原之后，作者们从新型冠状病毒的α、β和γ版本中找到抗体已经成功的证据，并据此开始进行反向工作。 </p> 
<p>他们使用这些数据来预测哪些突变的抗体能够延长疗效。 </p> 
<p>作者表示，我们的办法生成了一个用电脑模拟的抗体CDR的突变库，通过训练几何中立网络进行排序。这样不仅能提高抗体和Delta RBD的结合，还能维持抗体和其它所关注变体的RBD的结合。 </p> 
<p>CDR，全称为互补性决定区，是和抗原结合的一部分或是抗体。RBD，全称为受体结合区，是病毒上的重要靶点。 </p> 
<p>研究人员<a class="project-link" data-id="95377" data-name="得到" data-logo="https://img.36krcdn.com/20210807/v2_966db147ab4646ef82349f069ce61219_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/95377" target="_blank">得到</a>了双重、三重，甚至四重的变异抗体。他们在实验室里用合成的病毒来<a class="project-link" data-id="8712" data-name="测试" data-logo="https://img.36krcdn.com/20220318/v2_d188db412f2e4db89c6424314ac39971_img_jpg" data-refer-type="2" href="https://36kr.com/projectDetails/8712" target="_blank">测试</a>这些抗体。他们发现，随着突变的合成，降低抗原浓度的效果越来越强。 </p> 
<p>他们得出结论，认为存在一种物质能更好的让突变抗体和病毒相结合。 </p> 
<p>他们写道，「有三到四次突变的抗体HX001-020、HX001-033和HX001-034也比有两次突变的HX001-034要强。亲合力的提高可能会让这些抗体的中和活性在遇到非典或新冠的野生病毒或变体病毒时增加。」 </p> 
<p>有一个引人深思的发现是，一个突变的抗体能够避免病毒的突变，其目的是提高效率。在一份结构分析中，他们发现原始抗体的一部分和抗原的一个特定部分擦肩而过，二者相互排斥。 </p> 
<p>这是因为抗体的粒子R103和抗原的粒子R436都有非常长的侧链，并且都携带正电子，这两种粒子之间的亲和性会产生一种强大的推力，这股力量会削弱抗体和抗原之间的结合度。 </p> 
<p>科学家们替换普通的抗体粒子之后，就观察不到R346和Delta RBD的直接作用了。该因素也许能解释针对Delta变体的中和效果为什么能够大大改善。 </p> 
<p>作者们在研究的抗体正好是由Shan和他的同事们去年引入的。这一事实让整个研究变得更加有趣。 </p> 
<p>名叫P36-5D2的抗体是从一名患过新冠病毒的康复患者的血清中提取出来的。Shan和他的团队通过动物模型研究，发现这种抗体是一种适用面广、有效、具有保护性的抗体。 </p> 
<p>因此，这项新研究标志着人工智能领域的一个里程碑。即借助电脑，把传统的生物产品进行改进，从而扩展传统的生物安全实验室治疗传染性疾病的办法。 </p> 
<h2><strong>AlphaFold足以改变人类？</strong></h2> 
<p>2021年年底，人工智能预测蛋白质结构AlphaFold被评Science评为2021十大科学突破之首。 </p> 
<p>人工智能正在催生新的科研范式，AI for Science已经成为许多科学家的共识。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,950" src="https://img.36krcdn.com/20220321/v2_82db649cd53f48e8999a01ea6d79df99_img_000" referrerpolicy="no-referrer"></p> 
<p>长期以来，蛋白质都是生命科学工作者研究的重点。 </p> 
<p>因为蛋白质是生命活动的主要承担者，甚至毫不夸张的说，没有蛋白质就没有生命。 </p> 
<p>而其中，蛋白质的结构更是众多生命科学工作者研究的热点，毕竟其主要功能是由结构决定的。 </p> 
<p>2020年，AlphaFold2的问世成为生物学界海啸级的地震。 </p> 
<p>紧接着DeepMind开源了AlphaFold2，并能够预测出98.5%的蛋白质结构，让学术圈再次<a class="project-link" data-id="353171" data-name="沸腾" data-logo="https://img.36krcdn.com/20210811/v2_7087813349e94e70bd7e4bd86717e97d_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/353171" target="_blank">沸腾</a>。 </p> 
<p>不仅如此，研究人员还将其做成了数据集，将其免费开放。 </p> 
<p class="image-wrapper"><img data-img-size-val="1079,607" src="https://img.36krcdn.com/20220321/v2_acd5b37aa9294f69aa4322459c922a1f_img_000" referrerpolicy="no-referrer"></p> 
<p>对蛋白质进行系统深入的研究，能让人类从更深层次诠释生命体的构成和运作变化规律，进而全面揭示生命运行、发展的机制，激发生物科学、药物研发、合成生物学方面的发展。 </p> 
<p>另一方面，将人工智能方法应用到蛋白质预测，可以让科研人员从中得到许多借鉴，站在神经网络与深度学习的技术巨人的肩膀上，推动生物界的发展与研究。 </p> 
<h2><strong>「AI+生物」团队强强联合</strong></h2> 
<p>可以说，清华这个「AI+生物」的打造，是当前新冠中和抗体研究打造的最佳团队。 </p> 
<p>它充分利用了清华大学的校内科研资源优势，联合清华大学医学院与清华大学智能产业研究院（AIR），进行强强联合，「AI+生物」集中攻关。 </p> 
<p>张林琦教授，来自清华大学医学院，是该研究的领衔<a class="project-link" data-id="3969467" data-name="人物" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3969467" target="_blank">人物</a>之一。 </p> 
<p class="image-wrapper"><img data-img-size-val="214,234" src="https://img.36krcdn.com/20220321/v2_b09fedfa33404b12a5433b5810b73c05_img_000" referrerpolicy="no-referrer"></p> 
<p>此前，张林琦教授一直致力于挖掘新冠免疫保护机制，开创药物和疫苗研发。 </p> 
<p>据清华大学医学院官网介绍，张林琦教授于1992年获得英国爱丁堡大学分子病毒学博士学位，之后在美国纽约大学和洛克菲勒大学担任助理教授和副教授，2007年全职任教于清华大学，现为清华大学医学院长聘教授，北京协和医学院兼职教授，博士生导师，清华大学艾滋病综合研究中心主任。 </p> 
<p class="image-wrapper"><img data-img-size-val="680,370" src="https://img.36krcdn.com/20220321/v2_c10521145ef840d9a4cae42f52fe6751_img_000" referrerpolicy="no-referrer"></p> 
<p>张林琦教授是首位中国籍非洲科学院院士，于2016年当选。 </p> 
<p class="image-wrapper"><img data-img-size-val="327,200" src="https://img.36krcdn.com/20220321/v2_df7507ac4f3d43488daad4123f4a5b53_img_000" referrerpolicy="no-referrer"></p> 
<p>2014年非洲爆发了大规模的埃博拉病毒，作为国内外传染病研究专家，张林琦教授带着一名研究人员的初心和使命，致力于病毒研究。 </p> 
<p>然而，新冠病毒的肆虐远比我们想象地要猖狂！ </p> 
<p>面对这样的困境，研究人员毫不畏缩，大胆尝试，将计算机科学前沿成果与研究方法运用到传统生物研究上。 </p> 
<p>彭健，清华大学智能产业研究院高级访问教授，同样是该研究的领衔人物之一。 </p> 
<p class="image-wrapper"><img data-img-size-val="429,600" src="https://img.36krcdn.com/20220321/v2_ec7ff2b275554cdc9e5b6732f65bc53d_img_000" referrerpolicy="no-referrer"></p> 
<p>彭健博士的主要研究领域为信息学，他从生物化学领域找到了学科交叉点，在生物信息学、化学信息学和机器学习方面，包括蛋白质结构预测技术的关键测试（CASP），及转化医学和药物基因组学的DREAM 挑战等，取得了备受<a class="project-link" data-id="235198" data-name="瞩目" data-logo="https://img.36krcdn.com/20220120/v2_cbb026bcf908481eb30ba34ed8ffbfb6_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4461801211?mp=zzquote" target="_blank">瞩目</a>的成就。 </p> 
<p class="image-wrapper"><img data-img-size-val="1080,720" src="https://img.36krcdn.com/20220321/v2_93d78b71891a4d4190f8cc2ced9a8529_img_000" referrerpolicy="no-referrer"></p> 
<p>清华AIR引领人工智能赋能生命科学，这是吸引彭健博士加入清华大学智能产业研究院的重要原因 </p> 
<p>此前，彭健于2013年获芝加哥大学丰田技术学院计算机科学博士，接着，在MIT计算机科学与人工智能实验室从事博士后研究，然后，担任美国伊利诺伊大学厄巴纳-香槟分校计算机科学系副教授。 </p> 
<p>彭健说：「交叉学科人才的培养尤其重要」！这不，加入不到1年时间，就已开花结果。 </p> 
<p>参考资料：</p> 
<p>https://www.med.tsinghua.edu.cn/info/1049/3926.htm </p> 
<p>https://air.tsinghua.edu.cn/info/1001/1005.htm </p> 
<p>https://www.zdnet.com/article/mit-and-tsinghua-scholars-use-deepminds-alphafold-approach-to-boost-covid-19-antibodies/ </p> 
<p>https://www.pnas.org/doi/10.1073/pnas.2122954119 </p> 
<p>本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/-rAaBzeagSaWJgBIbJdNjQ">“新智元”（ID:AI_era）</a>，作者：新智元，编辑：桃子 拉燕 时光，36氪经授权发布。</p>  
</div>
            