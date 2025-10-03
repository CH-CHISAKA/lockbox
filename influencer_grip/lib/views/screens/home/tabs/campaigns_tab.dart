import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../../controllers/campaigns_controller.dart';
import '../../../../views/widgets/campaign_card.dart';

class CampaignsTab extends StatelessWidget {
  const CampaignsTab({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<CampaignsController>();
    return RefreshIndicator(
      onRefresh: controller.load,
      child: ListView.builder(
        padding: const EdgeInsets.all(16),
        itemCount: controller.campaigns.length,
        itemBuilder: (context, index) => Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: CampaignCard(campaign: controller.campaigns[index]),
        ),
      ),
    );
  }
}
