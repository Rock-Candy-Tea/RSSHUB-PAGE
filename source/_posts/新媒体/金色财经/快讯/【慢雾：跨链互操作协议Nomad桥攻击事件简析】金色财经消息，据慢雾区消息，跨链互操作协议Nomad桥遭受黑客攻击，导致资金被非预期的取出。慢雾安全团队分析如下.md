
---
title: '【慢雾：跨链互操作协议Nomad桥攻击事件简析】金色财经消息，据慢雾区消息，跨链互操作协议Nomad桥遭受黑客攻击，导致资金被非预期的取出。慢雾安全团队分析如下...'
categories: 
 - 新媒体
 - 金色财经
 - 快讯
headimg: 'https://picsum.photos/400/300?random=8474'
author: 金色财经
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=8474'
---

<div>   
【慢雾：跨链互操作协议Nomad桥攻击事件简析】金色财经消息，据慢雾区消息，跨链互操作协议Nomad桥遭受黑客攻击，导致资金被非预期的取出。慢雾安全团队分析如下： 
1. 在Nomad的Replica合约中，用户可以通过send函数发起跨链交易，并在目标链上通过process函数进行执行。在进行process操作时会通过acceptableRoot检查用户提交的消息必须属于是可接受的根，其会在prove中被设置。因此用户必须提交有效的消息才可进行操作。 
2. 项目方在进行Replica合约部署初始化时，先将可信根设置为0，随后又通过update函数对可信根设置为正常非0数据。Replica合约中会通过confirmAt映射保存可信根开始生效的时间以便在acceptableRoot中检查消息根是否有效。但在update新根时却并未将旧的根的confirmAt设置为0，这将导致虽然合约中可信根改变了但旧的根仍然在生效状态。 
3. 因此攻击者可以直接构造任意消息，由于未经过prove因此此消息映射返回的根是0，而项目方由于在初始化时将0设置为可信根且其并未随着可信根的修改而失效，导致了攻击者任意构造的消息可以正常执行，从而窃取Nomad桥的资产。 
综上，本次攻击是由于Nomad桥Replica合约在初始化时可信根被设置为0x0，且在进行可信根修改时并未将旧根失效，导致了攻击可以构造任意消息对桥进行资金窃取。  
</div>
            