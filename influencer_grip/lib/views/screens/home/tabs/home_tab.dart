import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../../controllers/home_controller.dart';
import '../../../../views/widgets/influencer_card.dart';
import '../../../../views/widgets/campaign_card.dart';

class HomeTab extends StatelessWidget {
  const HomeTab({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<HomeController>();

    return RefreshIndicator(
      onRefresh: controller.loadHomeData,
      child: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: const [
              Text('Discover', style: TextStyle(fontSize: 24, fontWeight: FontWeight.w700)),
              Icon(Icons.notifications_none)
            ],
          ),
          const SizedBox(height: 16),
          SizedBox(
            height: 42,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              itemCount: controller.categories.length,
              separatorBuilder: (_, __) => const SizedBox(width: 8),
              itemBuilder: (context, index) {
                final c = controller.categories[index];
                final selected = c == controller.selectedCategory;
                return ChoiceChip(
                  selected: selected,
                  label: Text(c),
                  onSelected: (_) => controller.selectCategory(c),
                );
              },
            ),
          ),
          const SizedBox(height: 16),
          const Text('Top Influencers', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
          const SizedBox(height: 12),
          SizedBox(
            height: 220,
            child: ListView.separated(
              scrollDirection: Axis.horizontal,
              itemCount: controller.influencers.length,
              separatorBuilder: (_, __) => const SizedBox(width: 12),
              itemBuilder: (context, index) => InfluencerCard(profile: controller.influencers[index]),
            ),
          ),
          const SizedBox(height: 16),
          const Text('Active Campaigns', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600)),
          const SizedBox(height: 12),
          ...controller.campaigns.map((c) => Padding(
                padding: const EdgeInsets.only(bottom: 12),
                child: CampaignCard(campaign: c),
              )),
        ],
      ),
    );
  }
}
