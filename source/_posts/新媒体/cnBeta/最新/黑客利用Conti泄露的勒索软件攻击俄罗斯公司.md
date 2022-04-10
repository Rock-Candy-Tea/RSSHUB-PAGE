
---
title: '黑客利用Conti泄露的勒索软件攻击俄罗斯公司'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2022/0410/9ab5d1e7666a087.png'
author: cnBeta
comments: false
date: Sun, 10 Apr 2022 12:16:03 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2022/0410/9ab5d1e7666a087.png'
---

<div>   
<strong>一个黑客组织利用Conti恶意软件集团泄露的勒索软件源代码创建了他们自己的勒索软件，然后用于对俄罗斯组织进行网络攻击。</strong>虽然经常听到勒索软件攻击公司并加密数据，但我们很少听到位于俄罗斯的黑客组织受到类似的攻击。这种缺乏攻击的情况是由于俄罗斯黑客普遍认为，如果他们不影响俄罗斯的利益，那么该国的执法部门将对攻击其他国家的行为视而不见。<br>
 <p>然而，现在情况发生了变化，一个被称为NB65的黑客组织现在专门以俄罗斯组织为目标进行勒索软件攻击。</p><p>过去一个月，一个名为NB65的黑客组织一直在入侵俄罗斯实体，窃取他们的数据，并将其泄露到网上，并警告说这些攻击是由于俄罗斯入侵乌克兰。</p><p><img src="https://static.cnbetacdn.com/article/2022/0410/9ab5d1e7666a087.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>据称被该黑客组织攻击的俄罗斯实体包括文件管理运营商Tensor，俄罗斯航天局，以及国有的俄罗斯<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https%3A%2F%2Flist.jd.com%2Flist.html%3Fcat%3D737%2C794%2C798%26ev%3D4155_76344%26sort%3Dsort_rank_asc%26trans%3D1%26JL%3D2_1_0%23J_crumbsBar" target="_blank">电视</a>和广播公司VGTRK。</p><p>对VGTRK的攻击尤其重要，它导致了据称786.2GB的数据被盗，其中包括90万封电子邮件和4000个文件，这些数据被公布在DDoS Secrets网站上。</p><p><img src="https://static.cnbetacdn.com/article/2022/0410/32780e4ec5202cb.png" title alt="图片.png" referrerpolicy="no-referrer"></p><p>最近，NB65黑客转向了一种新的战术--自3月底以来以俄罗斯组织为目标进行勒索软件攻击。</p><p>更有趣的是，该黑客组织使用泄露的Conti勒索软件操作的源代码创建了他们定制版本的勒索软件，这些来自俄罗斯的网络安全威胁行为始作俑者通常禁止其成员攻击俄罗斯的实体。</p><p>Conti的源代码是在他们在攻击乌克兰的问题上与俄罗斯站在一起之后泄露的，一位安全研究员泄露了17万条内部聊天信息和他们行动的源代码。</p><p>BleepingComputer首先通过威胁分析师Tom Malka了解到NB65的攻击，但我们找不到勒索软件的样本，而且该黑客组织也不愿意分享它。</p><p>然而，这种情况在昨天发生了变化，NB65修改过的Conti勒索软件可执行文件的样本被上传到VirusTotal，让我们得以一窥它的运作方式。</p><p><img src="https://static.cnbetacdn.com/article/2022/0410/75e4bb531cf7545.webp" title alt="encrypted-files.webp" referrerpolicy="no-referrer"></p><p>几乎所有的杀毒软件供应商都将VirusTotal上的这个样本检测为Conti，Intezer Analyze还确定它使用的代码与通常的Conti勒索软件样本有66%相同。</p><p>BleepingComputer给NB65的勒索软件做了一个测试，当加密文件时，它会在被加密文件的名称后加上.NB65的扩展名。</p><p>该勒索软件还将在整个加密设备中创建名为R3ADM3.txt的勒索信文本，威胁者将网络攻击归咎于总统弗拉基米尔·普京入侵乌克兰。</p><p>"我们正在密切关注。 你们的总统不应该犯下战争罪。"NB65勒索软件显示的说明中写道。</p><p>NB65黑客组织的一名代表表示，他们的加密器是基于第一个Conti源代码的泄漏，但因为改变了算法，所以现有的解密器将无法工作。</p><p>"它被修改后，所有版本的Conti解密器都无法工作。每次部署都会根据我们为每个目标改变的几个变量产生一个随机的密钥。如果不与我们联系，真的没有办法解密。"</p><p>目前，NB65还没有收到他们的受害者的任何通信，并告诉我们他们不期待任何通信。</p><p><img src="https://static.cnbetacdn.com/article/2022/0410/414921c3409aa1a.webp" title alt="ransom-note.webp" referrerpolicy="no-referrer"></p><p>至于NB65攻击俄罗斯组织的原因：</p><p>"在布查屠杀事件后之后，我们选择了针对某些公司，这些公司可能看上去是服务于民用市场的，但仍然会对俄罗斯的正常运作能力产生影响。 俄罗斯民众对普京的战争罪行的支持是压倒性的。 从一开始我们就明确表示。 我们在支持乌克兰。 我们将兑现我们的承诺。 当俄罗斯停止在乌克兰的所有敌对行动并结束这场荒谬的战争时，NB65将停止攻击俄罗斯互联网上的资产和公司。"</p><p>"我们将不会攻击俄罗斯以外的任何目标。 像Conti和Sandworm这样的组织，以及其他俄罗斯APT多年来一直通过勒索软件、供应链攻击（Solarwinds或国防承包商）来打击西方。我们认为现在是他们自己处理这个问题的时候了。"</p>   
</div>
            