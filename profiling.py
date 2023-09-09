def main():
    import cProfile
    import pstats
    import pagerank

    with cProfile.Profile() as pr:
        pagerank.pagerank_from_csv('email-Eu-core.txt-nodes.csv', 'email-Eu-core.txt-edges.csv', num_iterations=40)
        #pagerank.pagerank_from_csv('characters-nodes.csv', 'characters-edges.csv', num_iterations=40)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='pagerank_profiling.prof')
    # snakeviz ./pagerank_profiling.prof

if __name__ == '__main__':
    main()