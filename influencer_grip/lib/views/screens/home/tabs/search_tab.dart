import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../../controllers/search_controller.dart';
import '../../../../views/widgets/influencer_card.dart';

class SearchTab extends StatelessWidget {
  const SearchTab({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<SearchController>();

    return Padding(
      padding: const EdgeInsets.all(16),
      child: Column(
        children: [
          TextField(
            decoration: const InputDecoration(
              hintText: 'Search influencers, categories, campaigns...',
              prefixIcon: Icon(Icons.search),
            ),
            onChanged: controller.setQuery,
          ),
          const SizedBox(height: 16),
          Expanded(
            child: GridView.builder(
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 12,
                crossAxisSpacing: 12,
                childAspectRatio: 0.78,
              ),
              itemCount: controller.results.length,
              itemBuilder: (context, index) => InfluencerCard(profile: controller.results[index]),
            ),
          ),
        ],
      ),
    );
  }
}
